from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from .serializers import ConsultaSerializer
from ai_chats.models import AIChat
import os
from dotenv import load_dotenv

"""
OBS: Falta decidir o que fazer a respeito da leitura dos documentos, está sendo preciso
reiniciar a aplicação para atualizar o que a IA lê, para gerar as respostas atualizadas.

Ao rodar o projeto PRI, os PDFs que já estão no banco são o que a IA vai saber responder, 
se durante a execussão forem adicionados novos PDFs, será preciso reiniciar o projeto PRI,
para que a IA receba os novos embeddings dos novos documentos.
"""

# Configurações
DOCUMENTS_FOLDER = os.getenv('DOCUMENTS')

# Variáveis globais para armazenar os documentos e a base vetorial
documents = []
db = None

# Carregar documentos PDF de um diretório e extrair seu conteúdo
def carregar_documentos(diretorio):
    documentos = []
    for filename in os.listdir(diretorio):
        if filename.endswith(".pdf"):
            file_path = os.path.join(diretorio, filename)
            loader = PyMuPDFLoader(file_path=file_path)
            documentos.extend(loader.load())
    return documentos

# Inicializar documentos e embeddings na inicialização
def inicializar_sistema():
    global documents, db
    documents = carregar_documentos(DOCUMENTS_FOLDER)
    if documents:
        embedding = OpenAIEmbeddings()
        db = FAISS.from_documents(documents, embedding)
        print(f"{len(documents)} documentos carregados.")  # Verificando a quantidade de documentos carregados
    else:
        print("Nenhum documento foi carregado.")

# Inicialize o sistema de documentos e base vetorial
inicializar_sistema()

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

@api_view(['POST'])
@csrf_exempt
def consultar(request):
    serializer = ConsultaSerializer(data=request.data)

    if serializer.is_valid():
        user_message = serializer.validated_data.get('message')
        chat_id = request.data.get('chat_id')  # ID do chat para buscar configurações

        # Verificar se o chat_id foi passado e se existe um chat correspondente
        try:
            chat_config = AIChat.objects.get(id=chat_id)
        except AIChat.DoesNotExist:
            return Response({'error': 'Chat não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        # Obter configurações específicas do chat
        chat_temperature = chat_config.temperature
        chat_prompt = chat_config.prompt

        if not user_message:
            return Response({'error': 'A mensagem está vazia ou não foi fornecida.'}, status=status.HTTP_400_BAD_REQUEST)

        if not documents:
            return Response({'resposta': "Nenhum documento válido foi encontrado."}, status=status.HTTP_400_BAD_REQUEST)

        # Função para consultar a base
        def consulta_base(query):
            if not query:
                return []
            similares = db.similarity_search(query, k=5)
            return [doc.page_content for doc in similares]

        dados = consulta_base(user_message)

        if not dados:
            return Response({'resposta': "Não encontrei uma resposta coerente na base de dados. Por favor, reformule sua pergunta."}, status=status.HTTP_400_BAD_REQUEST)

        # Configurar o modelo LLM com a temperatura específica do chat
        llm = ChatOpenAI(temperature=chat_temperature, model="gpt-4", max_tokens=4000)

        # Template customizado com o prompt do chat
        template = f"""
        {chat_prompt}
        
        Aqui está a pergunta do usuário com relação aos dados enviados a você:
        {{message}}
        
        Dados relevantes encontrados nos documentos:
        {{dados}}
        """

        prompt = PromptTemplate(input_variables=["message", "dados"], template=template)

        # Atualizando para usar LLMChain
        chain = LLMChain(llm=llm, prompt=prompt)

        # Preparar dados para o modelo
        max_tokens = 4000
        dados_reduzidos = "\n".join(dados)
        if len(dados_reduzidos) > max_tokens:
            dados_reduzidos = dados_reduzidos[:max_tokens]

        try:
            # Executa a consulta de forma síncrona e retorna a resposta
            resposta = chain.run({"message": user_message, "dados": dados_reduzidos})
            return Response({'resposta': resposta})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({'error': 'Método inválido'}, status=status.HTTP_400_BAD_REQUEST)

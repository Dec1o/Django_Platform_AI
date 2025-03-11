<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django_Platform_AI - Documentação</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f4;
            color: #333;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #0056b3;
        }
        pre {
            background: #222;
            color: #fff;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            font-family: "Courier New", monospace;
        }
        a {
            color: #007bff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Django_Platform_AI - Documentação</h1>
    
    <h2>Visão Geral do Projeto 🚀</h2>
    <p>O <strong>Django_Platform_AI</strong> é uma aplicação web desenvolvida com o framework Django, que integra funcionalidades de inteligência artificial para aprimorar a interação com os usuários.</p>
    
    <h2>Tecnologias Utilizadas 🛠️</h2>
    <ul>
        <li><strong>Django</strong>: Framework web para desenvolvimento backend.</li>
        <li><strong>PostgreSQL</strong>: Banco de dados relacional utilizado na aplicação.</li>
        <li><strong>Django Rest Framework (DRF)</strong>: Implementação de APIs REST.</li>
        <li><strong>S3 da AWS</strong>: Armazenamento de arquivos na nuvem.</li>
        <li><strong>Selenium e Flask</strong>: Utilizados em integrações e automação.</li>
        <li><strong>LangChain e OpenAI</strong>: Ferramentas para processamento de linguagem natural (NLP) e IA.</li>
    </ul>

    <h2>Guia de Instalação e Execução ⚙️</h2>
    <h3>1. Clonar o Repositório</h3>
    <pre><code>git clone https://github.com/Dec1o/Django_Platform_AI.git
cd Django_Platform_AI</code></pre>

    <h3>2. Criar e Ativar um Ambiente Virtual</h3>
    <pre><code>python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows</code></pre>

    <h3>3. Instalar Dependências</h3>
    <pre><code>pip install -r requirements.txt</code></pre>

    <h3>4. Configurar o Banco de Dados PostgreSQL</h3>
    <p>Crie um banco de dados no PostgreSQL e configure as credenciais no arquivo <code>.env</code>.</p>

    <h3>5. Executar Migrações</h3>
    <pre><code>python manage.py migrate</code></pre>

    <h3>6. Criar Superusuário (Opcional)</h3>
    <pre><code>python manage.py createsuperuser</code></pre>

    <h3>7. Iniciar o Servidor</h3>
    <pre><code>python manage.py runserver</code></pre>
    <p>A aplicação estará disponível em <a href="http://127.0.0.1:8000/" target="_blank">http://127.0.0.1:8000/</a></p>
    
    <h2>Rotas Disponíveis 🌐</h2>
    <h3>1. ai_chats/</h3>
    <ul>
        <li>GET /ai_chats/: Lista todas as interações de chat.</li>
        <li>POST /ai_chats/: Cria uma nova interação de chat.</li>
        <li>GET /ai_chats/{id}/: Exibe detalhes de uma interação específica.</li>
        <li>PUT /ai_chats/{id}/: Atualiza uma interação existente.</li>
        <li>DELETE /ai_chats/{id}/: Remove uma interação.</li>
    </ul>

    <h3>2. companies/</h3>
    <ul>
        <li>GET /companies/: Lista todas as empresas.</li>
        <li>POST /companies/: Adiciona uma nova empresa.</li>
        <li>GET /companies/{id}/: Exibe detalhes de uma empresa específica.</li>
        <li>PUT /companies/{id}/: Atualiza informações de uma empresa.</li>
        <li>DELETE /companies/{id}/: Remove uma empresa.</li>
    </ul>

    <h3>3. files/</h3>
    <ul>
        <li>GET /files/: Lista todos os arquivos.</li>
        <li>POST /files/: Faz upload de um novo arquivo.</li>
        <li>GET /files/{id}/: Exibe detalhes de um arquivo específico.</li>
        <li>PUT /files/{id}/: Atualiza informações de um arquivo.</li>
        <li>DELETE /files/{id}/: Remove um arquivo.</li>
    </ul>
    
    <h2>Estrutura do Banco de Dados e Relacionamentos 📊</h2>
    <p>Cada aplicativo implementa operações CRUD para gerenciar suas respectivas entidades. As relações no banco de dados são estabelecidas utilizando os modelos do Django (<code>models.py</code>).</p>

    <h3>Exemplo de Relacionamentos</h3>
    <ul>
        <li><strong>Usuários e Empresas</strong>: Um usuário pode estar associado a uma ou mais empresas (Muitos-para-Muitos).</li>
        <li><strong>Arquivos e Grupos</strong>: Um arquivo pode pertencer a um grupo específico (Um-para-Muitos).</li>
        <li><strong>Chats e Usuários</strong>: Cada interação de chat está vinculada a um usuário (Muitos-para-Um).</li>
    </ul>

    <h2>Considerações Finais 🎯</h2>
    <p>O <strong>Django_Platform_AI</strong> é uma plataforma robusta que integra IA e funcionalidades de gerenciamento de arquivos, chats e usuários de forma modular.</p>
    <p>Para mais detalhes, consulte o repositório oficial no GitHub: <a href="https://github.com/Dec1o/Django_Platform_AI" target="_blank">Django_Platform_AI</a>.</p>
</body>
</html>

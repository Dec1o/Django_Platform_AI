# Django_Platform_AI - Documentação

## Visão Geral do Projeto 🚀
O **Django_Platform_AI** é uma aplicação web desenvolvida com o framework Django, que integra funcionalidades de inteligência artificial para aprimorar a interação com os usuários.

## Tecnologias Utilizadas 🛠️
- **Django**: Framework web para desenvolvimento backend.
- **PostgreSQL**: Banco de dados relacional utilizado na aplicação.
- **Django Rest Framework (DRF)**: Implementação de APIs REST.
- **S3 da AWS**: Armazenamento de arquivos na nuvem.
- **Selenium e Flask**: Utilizados em integrações e automação.
- **LangChain e OpenAI**: Ferramentas para processamento de linguagem natural (NLP) e IA.

## Guia de Instalação e Execução ⚙️

### 1. Clonar o Repositório
```bash
git clone https://github.com/Dec1o/Django_Platform_AI.git
cd Django_Platform_AI
```

### 2. Criar e Ativar um Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar o Banco de Dados PostgreSQL
Crie um banco de dados no PostgreSQL e configure as credenciais no arquivo `.env`.

### 5. Executar Migrações
```bash
python manage.py migrate
```

### 6. Criar Superusuário (Opcional)
```bash
python manage.py createsuperuser
```

### 7. Iniciar o Servidor
```bash
python manage.py runserver
```
A aplicação estará disponível em [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Rotas Disponíveis 🌐

### 1. `ai_chats/`
- `GET /ai_chats/`: Lista todas as interações de chat.
- `POST /ai_chats/`: Cria uma nova interação de chat.
- `GET /ai_chats/{id}/`: Exibe detalhes de uma interação específica.
- `PUT /ai_chats/{id}/`: Atualiza uma interação existente.
- `DELETE /ai_chats/{id}/`: Remove uma interação.

### 2. `companies/`
- `GET /companies/`: Lista todas as empresas.
- `POST /companies/`: Adiciona uma nova empresa.
- `GET /companies/{id}/`: Exibe detalhes de uma empresa específica.
- `PUT /companies/{id}/`: Atualiza informações de uma empresa.
- `DELETE /companies/{id}/`: Remove uma empresa.

### 3. `files/`
- `GET /files/`: Lista todos os arquivos.
- `POST /files/`: Faz upload de um novo arquivo.
- `GET /files/{id}/`: Exibe detalhes de um arquivo específico.
- `PUT /files/{id}/`: Atualiza informações de um arquivo.
- `DELETE /files/{id}/`: Remove um arquivo.

## Estrutura do Banco de Dados e Relacionamentos 📊
Cada aplicativo implementa operações CRUD para gerenciar suas respectivas entidades. As relações no banco de dados são estabelecidas utilizando os modelos do Django (`models.py`).

### Exemplo de Relacionamentos
- **Usuários e Empresas**: Um usuário pode estar associado a uma ou mais empresas (Muitos-para-Muitos).
- **Arquivos e Grupos**: Um arquivo pode pertencer a um grupo específico (Um-para-Muitos).
- **Chats e Usuários**: Cada interação de chat está vinculada a um usuário (Muitos-para-Um).

## Considerações Finais 🎯
O **Django_Platform_AI** é uma plataforma robusta que integra IA e funcionalidades de gerenciamento de arquivos, chats e usuários de forma modular.

Para mais detalhes, consulte o repositório oficial no GitHub: [Django_Platform_AI](https://github.com/Dec1o/Django_Platform_AI).


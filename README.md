Django MVT Platform + AI Microservices, developed by: Décio Carvalho Faria.
# Django_Platform_AI - Documentation:

## Project Overview 🚀
**Django_Platform_AI** is a web application developed with the Django framework, which integrates artificial intelligence features to improve user interaction.

## Technologies Used 🛠️
- **Django**: Web framework for backend development.
- **PostgreSQL**: Relational database used in the application.
- **Django Rest Framework (DRF)**: Implementation of REST APIs.
- **AWS S3**: Cloud file storage.
- **Selenium and Flask**: Used in integrations and automation.
- **LangChain and OpenAI**: Tools for natural language processing (NLP) and AI.

## Database & ORM 🔗
Django's ORM is used to manage CRUD operations, maintaining data integrity and implementing relationships between entities. Queries are optimized to ensure efficiency, and the data model follows best practices for relational databases.

## Installation and Execution Guide ⚙️

### 1. Clone the Repository
```bash
git clone https://github.com/Dec1o/Django_Platform_AI.git
cd Django_Platform_AI
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the PostgreSQL Database
Create a database in PostgreSQL and configure the credentials in the `.env` file.

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 7. Start the Server
```bash
python manage.py runserver
```
The application will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Available Routes 🌐

### 1. `ai_chats/`
- `GET /ai_chats/`: Lists all chat interactions.
- `POST /ai_chats/`: Creates a new chat interaction.
- `GET /ai_chats/{id}/`: Displays details of a specific interaction. - `PUT /ai_chats/{id}/`: Updates an existing interaction.
- `DELETE /ai_chats/{id}/`: Removes an interaction.

### 2. `companies/`
- `GET /companies/`: Lists all companies.
- `POST /companies/`: Adds a new company.
- `GET /companies/{id}/`: Displays details for a specific company.
- `PUT /companies/{id}/`: Updates company information.
- `DELETE /companies/{id}/`: Removes a company.

### 3. `files/`
- `GET /files/`: Lists all files.
- `POST /files/`: Uploads a new file.
- `GET /files/{id}/`: Displays details for a specific file.
- `PUT /files/{id}/`: Updates file information.
- `DELETE /files/{id}/`: Removes a file.

## Database Structure and Relationships 📊
Each application implements CRUD operations to manage its respective entities. Relationships in the database are established using Django models (`models.py`).

### Relationship Example
- **Users and Companies**: A user can be associated with one or more companies (Many-to-Many).
- **Files and Groups**: A file can belong to a specific group (One-to-Many).
- **Chats and Users**: Each chat interaction is linked to a user (Many-to-One).

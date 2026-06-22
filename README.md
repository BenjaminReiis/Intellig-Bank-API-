# 🏦 Bank API

Uma API RESTful de um sistema bancário desenvolvida com **FastAPI**, simulando as principais funcionalidades de um banco digital moderno.

Este projeto foi criado com foco em boas práticas de desenvolvimento Backend, organização de código e arquitetura escalável, sendo ideal para portfólio e estudos.

---

## 🚀 Funcionalidades

### 👤 Autenticação

* Cadastro de usuários
* Login com autenticação JWT
* Senhas criptografadas com Bcrypt
* Rotas protegidas por Token Bearer

### 🏦 Contas Bancárias

* Criação de conta bancária
* Consulta de saldo
* Consulta dos dados da conta

### 💰 Operações Financeiras

* Depósito
* Saque
* Transferência entre contas
* Histórico de transações
* Extrato bancário

---

## 🛠 Tecnologias Utilizadas

* Python 3
* FastAPI
* SQLAlchemy 2.0
* Pydantic v2
* JWT (JSON Web Token)
* Passlib (Bcrypt)
* SQLite (desenvolvimento)
* PostgreSQL (produção)
* Uvicorn
* Docker
* Alembic

---

## 📂 Estrutura do Projeto

```text
bank-api/
│
├── app/
│   ├── core/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   ├── __init__.py
│   └── database.py
│
├── tests/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── main.py
```

---

## ▶️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/bank-api.git
```

### 2. Acesse a pasta

```bash
cd bank-api
```

### 3. Crie um ambiente virtual

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute a aplicação

```bash
uvicorn main:app --reload
```

---

## 📖 Documentação da API

Após iniciar o servidor, acesse:

* Swagger UI: `http://127.0.0.1:8000/docs`
* ReDoc: `http://127.0.0.1:8000/redoc`

---

## 📌 Funcionalidades Planejadas

* Transferência entre contas
* Extrato completo
* Docker
* PostgreSQL
* Alembic
* Testes automatizados
* Deploy no Render
* GitHub Actions (CI/CD)

---

## 🎯 Objetivo

Este projeto foi desenvolvido para praticar conceitos modernos de desenvolvimento Backend utilizando FastAPI e servir como projeto de portfólio para oportunidades de trabalho como Desenvolvedor Backend Python.

---

## 👨‍💻 Autor

**Benjamin Reis**

* Backend Developer
* Python
* FastAPI
* Java
* SQL
* APIs REST

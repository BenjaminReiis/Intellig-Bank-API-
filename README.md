<div align="center">

# 🏦 Bank API
### Sistema Bancário Digital | API RESTful com FastAPI

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?style=flat&logo=python&logoColor=white)](https://www.sqlalchemy.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-v2-E92063?style=flat&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![JWT](https://img.shields.io/badge/Auth-JWT-black?style=flat&logo=jsonwebtokens&logoColor=white)](https://jwt.io/)
[![SQLite](https://img.shields.io/badge/SQLite-dev-003B57?style=flat&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](#-licença)

**Uma API RESTful de sistema bancário, simulando as principais funcionalidades de um banco digital moderno — autenticação segura, contas, depósitos, saques e transferências.**

[Demonstração](#-demonstração) •
[Funcionalidades](#-funcionalidades) •
[Stack](#-tecnologias-utilizadas) •
[Instalação](#%EF%B8%8F-como-executar) •
[Endpoints](#-documentação-da-api) •
[Roadmap](#-roadmap)

</div>

---

## 🌐 Demonstração

| Recurso | Link |
|---|---|
| 🖥️ **Página do Projeto** | [benjaminreiis.github.io/Intellig-Bank-API-](https://benjaminreiis.github.io/Intellig-Bank-API-/) |
| 📦 **Repositório** | `github.com/benjaminreiis/bank-api` |

> 🚧 O deploy em nuvem (Render) ainda não está ativo — veja a seção [Roadmap](#-roadmap). Por enquanto, a API roda localmente seguindo as instruções abaixo.

---

## 🧠 Sobre o Projeto

A **Bank API** é uma API RESTful que simula um sistema bancário digital, desenvolvida com **FastAPI**. O projeto foi criado com foco em **boas práticas de desenvolvimento backend**, organização de código em camadas e arquitetura escalável — sendo ideal tanto para estudo de conceitos avançados quanto como peça de portfólio.

A aplicação reproduz o fluxo essencial de um banco moderno: cadastro de usuários, autenticação segura, abertura de contas e movimentações financeiras (depósito, saque e transferência), com histórico completo de transações.

---

## ✨ Funcionalidades

### 👤 Autenticação
- Cadastro de usuários
- Login com autenticação **JWT**
- Senhas criptografadas com **Bcrypt**
- Rotas protegidas por **Token Bearer**

### 🏦 Contas Bancárias
- Criação de conta bancária
- Consulta de saldo
- Consulta dos dados da conta

### 💰 Operações Financeiras
- Depósito
- Saque
- Histórico de transações

---

## 🛠 Tecnologias Utilizadas

| Tecnologia | Função no projeto |
|---|---|
| **Python 3** | Linguagem principal da aplicação |
| **FastAPI** | Framework web para construção da API REST |
| **SQLAlchemy 2.0** | ORM para modelagem e acesso ao banco de dados |
| **Pydantic v2** | Validação e tipagem dos dados de entrada/saída |
| **JWT** | Geração e validação de tokens de autenticação |
| **Passlib (Bcrypt)** | Hash seguro de senhas |
| **SQLite** | Banco de dados em ambiente de desenvolvimento |
| **PostgreSQL** | Banco de dados em ambiente de produção *(planejado)* |
| **Uvicorn** | Servidor ASGI responsável por executar a aplicação |
| **Docker** | Containerização da aplicação *(planejado)* |
| **Alembic** | Gerenciamento de migrations do banco de dados *(planejado)* |

---

## 📂 Estrutura do Projeto

```text
bank-api/
│
├── app/
│   ├── core/          # Configurações, segurança (JWT, hash), settings
│   ├── models/         # Modelos SQLAlchemy (User, Account, Transaction)
│   ├── routers/        # Rotas da API (auth, accounts, transactions)
│   ├── schemas/        # Schemas Pydantic (validação de entrada/saída)
│   ├── services/       # Regras de negócio e orquestração
│   ├── utils/           # Funções auxiliares
│   ├── __init__.py
│   └── database.py      # Configuração de conexão com o banco
│
├── tests/                # Testes automatizados
│
├── .env                   # Variáveis de ambiente
├── .gitignore
├── README.md
├── requirements.txt
└── main.py                # Ponto de entrada da aplicação
```

---

## ▶️ Como Executar

### Pré-requisitos
- [Python 3.11+](https://www.python.org/downloads/)
- `pip` instalado

### 1. Clone o repositório
```bash
git clone https://github.com/benjaminreiis/bank-api.git
```

### 2. Acesse a pasta do projeto
```bash
cd bank-api
```

### 3. Crie e ative um ambiente virtual

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

### 5. Configure as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto:
```env
SECRET_KEY=troque-esta-chave-em-produção
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
DATABASE_URL=sqlite:///./bank.db
```

### 6. Execute a aplicação
```bash
uvicorn main:app --reload
```

A API estará disponível em **`http://127.0.0.1:8000`**.

---

## 📖 Documentação da API

Após iniciar o servidor, acesse a documentação interativa:

| Ferramenta | URL |
|---|---|
| **Swagger UI** | `http://127.0.0.1:8000/docs` |
| **ReDoc** | `http://127.0.0.1:8000/redoc` |

A documentação permite testar todos os endpoints diretamente pelo navegador.

### Visão Geral dos Endpoints

| Método | Rota | Descrição | Autenticação |
|---|---|---|---|
| `POST` | `/auth/register` | Cadastra um novo usuário | ❌ |
| `POST` | `/auth/login` | Autentica e retorna o token JWT | ❌ |
| `POST` | `/accounts` | Cria uma nova conta bancária | ✅ |
| `GET` | `/accounts/me` | Consulta os dados da conta do usuário logado | ✅ |
| `GET` | `/accounts/me/balance` | Consulta o saldo atual | ✅ |
| `POST` | `/transactions/deposit` | Realiza um depósito na conta | ✅ |
| `POST` | `/transactions/withdraw` | Realiza um saque da conta | ✅ |
| `GET` | `/transactions/history` | Lista o histórico de transações | ✅ |

---

<details>
<summary><code>POST /auth/register</code> — Cadastrar usuário</summary>

```json
// Request
{
  "full_name": "João da Silva",
  "email": "joao@email.com",
  "password": "senha-super-segura"
}
```
```json
// Response 201 Created
{
  "id": 1,
  "full_name": "João da Silva",
  "email": "joao@email.com",
  "created_at": "2026-06-29T10:00:00Z"
}
```
</details>

<details>
<summary><code>POST /auth/login</code> — Autenticação</summary>

```json
// Request
{
  "email": "joao@email.com",
  "password": "senha-super-segura"
}
```
```json
// Response 200 OK
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```
</details>

<details>
<summary><code>POST /accounts</code> — Criar conta bancária</summary>

> 🔐 Requer `Authorization: Bearer <token>`

```json
// Response 201 Created
{
  "account_id": "acc_8f1a2b",
  "owner_id": 1,
  "balance": 0.0,
  "created_at": "2026-06-29T10:02:00Z"
}
```
</details>

<details>
<summary><code>GET /accounts/me/balance</code> — Consultar saldo</summary>

> 🔐 Requer `Authorization: Bearer <token>`

```json
// Response 200 OK
{
  "account_id": "acc_8f1a2b",
  "balance": 1500.75
}
```
</details>

<details>
<summary><code>POST /transactions/deposit</code> — Depósito</summary>

> 🔐 Requer `Authorization: Bearer <token>`

```json
// Request
{
  "amount": 500.00
}
```
```json
// Response 200 OK
{
  "transaction_id": "txn_001",
  "type": "DEPOSIT",
  "amount": 500.00,
  "balance_after": 2000.75,
  "created_at": "2026-06-29T10:05:00Z"
}
```
</details>

<details>
<summary><code>POST /transactions/withdraw</code> — Saque</summary>

> 🔐 Requer `Authorization: Bearer <token>`

```json
// Request
{
  "amount": 200.00
}
```
```json
// Response 200 OK
{
  "transaction_id": "txn_002",
  "type": "WITHDRAW",
  "amount": 200.00,
  "balance_after": 1800.75,
  "created_at": "2026-06-29T10:07:00Z"
}
```
```json
// Response 422 Unprocessable Entity (saldo insuficiente)
{
  "detail": "Saldo insuficiente para realizar o saque"
}
```
</details>

<details>
<summary><code>GET /transactions/history</code> — Extrato bancário</summary>

> 🔐 Requer `Authorization: Bearer <token>`

```json
// Response 200 OK
[
  {
    "transaction_id": "txn_001",
    "type": "DEPOSIT",
    "amount": 500.00,
    "created_at": "2026-06-29T10:05:00Z"
  },
  {
    "transaction_id": "txn_002",
    "type": "WITHDRAW",
    "amount": 200.00,
    "created_at": "2026-06-29T10:07:00Z"
  }
]
```
</details>

### Códigos de Status HTTP

| Código | Significado |
|---|---|
| `200` | Requisição bem-sucedida |
| `201` | Recurso criado com sucesso |
| `400` | Requisição inválida |
| `401` | Token ausente, inválido ou expirado |
| `404` | Recurso não encontrado |
| `422` | Erro de validação ou regra de negócio violada (ex: saldo insuficiente) |

---

## 🔐 Segurança

- Senhas nunca são armazenadas em texto puro — sempre com **hash Bcrypt**
- Autenticação via **JWT**, com expiração configurável de token
- Todas as rotas sensíveis (contas e transações) exigem **Token Bearer** válido
- Validação estrita de payloads via **Pydantic v2**, prevenindo dados malformados

---

## 🗺️ Roadmap

Funcionalidades planejadas para as próximas versões:

- [ ] Transferência entre contas
- [ ] Extrato completo com filtros por data e tipo de transação
- [ ] Containerização com **Docker**
- [ ] Migração para **PostgreSQL** em produção
- [ ] Gerenciamento de schema com **Alembic**
- [ ] Testes automatizados (Pytest)
- [ ] Deploy em nuvem (**Render**)
- [ ] Pipeline de **CI/CD** com GitHub Actions

---

## 🎯 Objetivo

Este projeto foi desenvolvido para praticar conceitos modernos de desenvolvimento backend utilizando **FastAPI**, servindo também como projeto de portfólio para oportunidades de trabalho como **Desenvolvedor Backend Python**.

---

## 🤝 Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch (`git checkout -b feature/minha-feature`)
3. Commit suas alterações (`git commit -m 'feat: adiciona minha feature'`)
4. Push para a branch (`git push origin feature/minha-feature`)
5. Abra um Pull Request

---

## 👨‍💻 Autor

**Benjamin Reis**

Backend Developer — Python · FastAPI · Java · SQL · APIs REST

[![GitHub](https://img.shields.io/badge/GitHub-benjaminreiis-181717?style=flat&logo=github&logoColor=white)](https://github.com/benjaminreiis)

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<div align="center">

⭐ Se este projeto foi útil, considere deixar uma estrela no repositório!

</div>

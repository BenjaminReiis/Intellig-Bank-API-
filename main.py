from fastapi import FastAPI

from app.database import Base, engine

# Importa todos os modelos para que o SQLAlchemy registre as tabelas
from app.models.user import User
from app.models.account import Account
from app.models.transaction import Transaction

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="🏦 Bank API",
    version="1.0.0",
    description="API REST de um sistema bancário desenvolvida com FastAPI."
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Bank API",
        "status": "online",
        "docs": "/docs"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }

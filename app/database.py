from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Cliente
from pathlib import Path

# Defina as constantes no início do arquivo
SQLITE_ORIGEM = "sqlite:///banco_origem.db"
SQLITE_DESTINO = "sqlite:///banco_destino.db"


def criar_bancos_exemplo():
    """Cria bancos de dados de exemplo com dados fictícios"""
    # Cria banco de origem
    engine_origem = create_engine(SQLITE_ORIGEM)
    Base.metadata.create_all(engine_origem)

    # Insere dados de exemplo
    Session = sessionmaker(bind=engine_origem)
    with Session() as session:
        session.add_all([
            Cliente(nome="João Silva", email="joao@xpinc.com", saldo=5000),
            Cliente(nome="Maria Souza", email="maria@xpinc.com", saldo=15000)
        ])
        session.commit()

    # Cria banco destino vazio
    engine_destino = create_engine(SQLITE_DESTINO)
    Base.metadata.create_all(engine_destino)

    print("✅ Bancos criados com sucesso!")
    print(f"- Origem: {Path('banco_origem.db').absolute()}")
    print(f"- Destino: {Path('banco_destino.db').absolute()}")


def migrar_dados():
    """Migra dados entre os bancos"""
    engine_origem = create_engine(SQLITE_ORIGEM)
    engine_destino = create_engine(SQLITE_DESTINO)

    SessionOrigem = sessionmaker(bind=engine_origem)
    SessionDestino = sessionmaker(bind=engine_destino)

    with SessionOrigem() as sessao_origem, SessionDestino() as sessao_destino:
        clientes = sessao_origem.query(Cliente).all()

        for cliente in clientes:
            sessao_destino.add(Cliente(
                nome=cliente.nome,
                email=cliente.email,
                saldo=cliente.saldo
            ))

        sessao_destino.commit()
        print(f"✅ {len(clientes)} clientes migrados!")


if __name__ == "__main__":
    criar_bancos_exemplo()
from sqlalchemy import Column, String, REAL, BIGINT
from src.settings.base import Base

class PessoaFisicaTable(Base):
    id = Column(BIGINT, primary_key=True)
    renda_mensal = Column(REAL, nullable= False)
    idade = Column(BIGINT, nullable= False)
    nome_completo = Column(String, nullable= False)
    celular = Column(String, nullable=False)
    email = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    saldo = Column(REAL, nullable=False)

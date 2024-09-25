from sqlalchemy import Column, String, BIGINT, REAL
from src.settings.base import Base

class PessoaJuridicaTable(Base):
    id = Column(BIGINT, primary_key=True)
    faturamento = Column(REAL, nullable= False)
    idade = Column(BIGINT, nullable= False)
    nome_fantasia = Column(String, nullable= False)
    celular = Column(String, nullable=False)
    email_corporativo = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    saldo = Column(REAL, nullable=False)

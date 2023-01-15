import sqlalchemy as sa

from datetime import datetime

from models.model_base import ModelBase

class Sabor(ModelBase):
    __tablename__: str = 'sabores'

    id: int = sa.column(sa.BigInteger, primary_key=True,autoincrement=True)
    data_criacao: datetime = sa.column(sa.DateTime, default=datetime.now, index=True)
    nome: str = sa.column(sa.String(45), unique=True, nullable=False)
    
    
    def __repr__(self) -> str:
        return f'<Sabor: {self.nome}>'
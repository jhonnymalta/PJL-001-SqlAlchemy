import sqlalchemy as sa
import sqlalchemy.orm as orm
from datetime import datetime

from models.model_base import ModelBase
from models.tipo_picole import TipoPicole

class Lote(ModelBase):
    __tablename__: str = 'lotes'

    id: int = sa.column(sa.BigInteger, primary_key=True,autoincrement=True)
    data_criacao: datetime = sa.column(sa.DateTime, default=datetime.now, index=True)

    id_tipo_picole: int = sa.column(sa.Integer,sa.ForeignKey('tipos_picole.id'))
    tipo_picolo: TipoPicole = orm.relationship('TipoPicole',lazy='joined')
    
    quantidade: int = sa.column(sa.Integer, nullable=False)
    def __repr__(self) -> str:
        return f'<Lote: {self.nome}>'
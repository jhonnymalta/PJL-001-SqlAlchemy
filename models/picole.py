import sqlalchemy as sa
import sqlalchemy.orm as orm

from datetime import datetime
from typing import List,Optional

from models.model_base import ModelBase
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.aditivo_nutritivo import AditivoNutritivo


#Picole pode ter varios ingredientes
ingredientes_picole = sa.Table(
    'ingredientes_picole',
    ModelBase.metadata,
    sa.Column('id_picole',sa.Integer,sa.ForeignKey('picoles.id')),
    sa.Column('id_ingrediente',sa.Integer,sa.ForeignKey('ingredientes.id'))
)
#picole pode ter varios aditivos nutritivos
aditivos_nutritivos_picole = sa.Table(
    'ditivos_nutritivos_picole',
    ModelBase.metadata,
    sa.Column('id_picole',sa.Integer,sa.ForeignKey('picoles.id')),
    sa.Column('id_aditivo_nutritivo',sa.Integer,sa.ForeignKey('aditivos_nutritivos.id'))
)


class Picole(ModelBase):
    __tablename__: str = 'picoles'

    id: int = sa.Column(sa.BigInteger, primary_key=True,autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    preco: float = sa.Column(sa.DECIMAL(8,2),  nullable=False)

    id_tipo_embalagem: int = sa.Column(sa.Integer,sa.ForeignKey('tipos_embalagem.id'))
    tipo_embalegem: TipoEmbalagem = orm.relationship('TipoEmbalagem',lazy='joined')

    id_sabor: int = sa.Column(sa.Integer,sa.ForeignKey('sabores.id'))
    sabor: Sabor = orm.relationship('Sabor',lazy='joined')
    
    id_tipo_picole: int = sa.Column(sa.Integer,sa.ForeignKey('tipo_picoles.id'))
    tipo_picole: TipoPicole = orm.relationship('TipoPicole',lazy='joined')


    #um picole pode ter vario ingredientes
    ingredientes: List[Ingrediente] = orm.relationship('Ingrediente',secondary=ingredientes_picole, backref='ingreditente',lazy='joined')
    
    #um picole pode ter vario ingredientes
    aditivos_nutritivos: Optional[List[AditivoNutritivo]] = orm.relationship('AditivoNutritivo',secondary=aditivos_nutritivos_picole, backref='aditivo_nutritivo',lazy='joined')
    
    def __repr__(self) -> str:
        return f'<Picole: {self.nome} com sabor {self.sabor.nome} e preço {self.preco}>'
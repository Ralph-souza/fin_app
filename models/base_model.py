# A model é basicamente o formato que queremos no nosso BD, estabelecemos as colunas e os tipos dos atributos
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

# O método declarative_base serve para permitir a declaração simultânea de 3(três) pontos do projeto ao mesmo tempo
# São eles: a tabela, o método mapper() e a classe ou objeto
Base = declarative_base()


# A classe BaseModel receberá apenas a tabela do banco para referência e o atributo em comum entre as demais
# entidades neste caso o 'ID_'
class BaseModel(Base):

    # Aplicações que usam mais de uma engine usam __abstract__ com o intuito de pertmitir o uso exclusivo de um
    # subset de atributos
    __abstract__ = True

    # Definição de colunas e parâmetros a serem atendidos na construção dos atributos
    id_ = Column('id_', Integer, primary_key=True)

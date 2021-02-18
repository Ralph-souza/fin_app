from sqlalchemy import Column, Integer, String
from models.base_model import BaseModel


# Definimos uma entidade 'User' a qual irá herdar 'BaseModel', definimos a tabela que irá receber os dados
# e definimos os atributos para a entidade.
class User(BaseModel):

    # Tabela que receberá os dados
    __tablename__ = "user"

    # Os atributos são registrados como variáveis e estão definidos com os seguintes parâmetros
    # Column: definido que haverá uma coluna para name o qual terá no máximo 50 caractéres e não nulos
    # Integer: esta coluna irá receber valores (numéricos) inteiros
    name = Column(String(50), nullable=False)
    age = Column(Integer(2), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)

    # métod reservado, ou mais comumente conhecido como 'Contructor', o __init__ faz parte dos conceito de
    # Programação Orientada à Objetos, esse método é chamado quando um obejto é criado a partir de uma classe
    # e permite a inicialização dos atributos de uma classe
    def __init__(self, name: str, age: int, phone: str, email: str) -> None:
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email

    # O decorator @property serve para atribuir de maneira  "oculta" setters e getters
    # Através do decorator podemos 3(três métodos escpecíficos: getter, setter, deleter
    @property
    # métodos get terão retorno
    def get_name(self) -> None:
        return self.name

    @name.setter
    # métodos set não possuem retorno, apenas dão set nos atributos
    def set_name(self, name) -> str:
        self.name = name

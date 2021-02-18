# A DAO (Data Access Object) acessa os objetos do banco registrados através da MODEL
# Primeiramente importamos o objeto 'USER' e posteriormente a BaseDao que possui as funções a serem executadas
from models.user_model import User
from dao.base_dao import BaseDao


# UseDao irá herdar as funcionalidade de BaseDao (save, read_all, read_by_id, delete)
class UserDao(BaseDao):
    def __init__(self):

        # O super() faz com que a função também adquira os atributos de 'USER'
        super().__init__(User)

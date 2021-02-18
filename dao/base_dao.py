# BaseDao deverá herdar as funções de conexão da sessão e as funções da BaseModel
from dao.session import Session
from models.base_model import BaseModel


class BaseDao:
    def __init__(self, type_model) -> None:
        self.__type_model = type_model

    def save(self, model: BaseModel) -> BaseModel:
        with Session() as session:
            session.add(model)

            # .commit() serve para registrar uma ação durante a sessão
            session.commit()

            # .refresh() serve para renovar os valores do DB
            session.refresh(model)
            return model

    # Herdando as características de BaseModel podemos filtrar ou ordenar por um atributo neste caso "ID_"
    def read_by_id(self, id_: int) -> BaseModel:
        if isinstance(id_, int):
            with Session() as session:

                # Aqui fazemos uma pesquisa (query) no objeto de '__type_model' filtramos por ID (um a um)
                # trazendo sempre a partir do primeiro
                result = session.query(self.__type_model).filter_by(id_=id_).first()
            return result
        else:
            raise TypeError('ID must be integer.')

    def read_all(self) -> list:
        with Session() as session:

            # Herdando as características de BaseModel podemos ordenar por "ID_" trazendo todos o atributos
            result = session.query(self.__type_model).order_by('id_').all()
        return result

    def delete(self, model: BaseModel) -> None:
        with Session() as session:
            result = session.delete(model)
            session.commit()

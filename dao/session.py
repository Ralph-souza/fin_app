# A session estabelece a concexão com o BD onde estarão guardados os dados
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Session:
    # A primeira função estabelece a conexão com o BD
    def __init__(self):
        connector = 'mysql+pymysql'
        host = 'mysql09-farm15.uni5.net'
        user = 'topskills17'
        password = 'ButecoOlist21'
        dbname = 'topskills17'
        self.__conn_string = f"{connector}://{user}:{password}@{host}:3306/{dbname}"

    # A função abaixo acessa a sessão com o BD
    def __enter__(self):
        self.__engine = create_engine(self.__conn_string)
        Session = sessionmaker(self.__engine)
        self.__session = Session()
        return self.__session

    # Utiliza-se close() para se fechar a sessão e dispose() para desfazer a engine criada
    def __exit__(self, type, value, traceback):
        self.__session.close()
        self.__engine.dispose()

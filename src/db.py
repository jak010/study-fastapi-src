from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

from sqlalchemy.orm import sessionmaker, Session, scoped_session


def get_url() -> URL:
    return URL.create(
        drivername="mysql+pymysql",
        username='root',
        password="1234",
        database="fastapi",
        host="127.0.0.1",
        port=9901
    )


class Connection:

    def __init__(self):
        self.url = get_url()



    @property
    def session(self) -> Session:
        engine = create_engine(self.url, echo=True)



        _Session = sessionmaker(bind=engine)
        session = _Session()
        return session

from functools import wraps

from dependency_injector.wiring import inject, Provide

from src.config.ioc import RepositoryConatiner
from sqlalchemy.orm import Session


def Transactional(func):
    @wraps(func)
    @inject
    def wrapper(*args,
                session: Session = Provide[RepositoryConatiner.session],
                **kwargs):

        try:
            f = func(*args, **kwargs)
            session.commit()
            return f
        except Exception as e:

            session.rollback()
            raise e
        finally:
            session.flush()
            session.close()

    return wrapper

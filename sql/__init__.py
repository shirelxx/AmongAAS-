import logging

from sqlalchemy import create_engine
from postgres_deployment import Base

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)

user = 'postgres'
password = 'postgres'
host = 'localhost:5432'
database = 'amongoass_db'


def get_db_engine():
    engine = create_engine(
        'postgresql+psycopg2://{0}:{1}@{2}/{3}'.format(user, password, host, database))
    Base.metadata.create_all(engine)
    return engine


while True:
    try:
        db_engine = get_db_engine().connect()
        if db_engine:
            break
    except Exception as e:
        LOGGER.warning(f"++++ Retrying connection to the database because of the issue {str(e)}++++")

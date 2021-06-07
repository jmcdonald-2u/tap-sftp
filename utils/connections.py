import logging
import sqlalchemy as sa
from functools import lru_cache

logging.basicConfig(format='%(asctime)s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO)
log = logging.getLogger(__name__)

@lru_cache(maxsize=1)
def sa_connection(**connection_string):
    """Create sqlalchemy connection to database."""
    if connection_string:
        dsn = '{engine}+psycopg2://{username}:{password}@{host}:{port}/{dbname}?sslmode=prefer'.format(**connection_string)
        log.info('Creating sql connection...')
    else:
        log.debug(f'Getting dsn for {connection_string}')
    try:
        con = sa.create_engine(dsn)
        log.info('Successfully connected to {host}'.format(**connection_string))
    except Exception as e:
        log.error(e)
        raise e
    return con

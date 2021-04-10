# FEED
FEED_URL = 'https://www.feedforall.com/sample.xml'

# DB
POSTGRES_HOST = '0.0.0.0'
POSTGRES_PORT = 5432
POSTGRES_USER = 'postgres'
POSTGRES_PASS = 'postgres'
POSTGRES_DB = 'feed_parser'

POSTGRES_DB_CONN = "postgresql://{}:{}@{}:5432/{}"\
    .format(POSTGRES_USER, POSTGRES_PASS, POSTGRES_HOST, POSTGRES_PORT , POSTGRES_DB)
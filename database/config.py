import os
import psycopg2
import urllib.parse as urlparse

url = urlparse.urlparse(os.environ['DATABASE_URL'])

DB_CONFIG = {
    'dbname': url.path[1:],
    'user': url.username,
    'password': url.password,
    'host': url.hostname,
    'port': url.port
}

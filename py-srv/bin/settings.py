user = 'maria'
password = 'pass'
host = 'db'
database = 'animal'

COCKROACH = {
    'engine': 'cockroachdb',
    'username': 'root',
    'password': '',
    'host': host,
    'db_name': database,
}

MYSQL = {
    'engine': 'mariadb+pymysql',
    'username': user,
    'password': password,
    'host': host,
    'db_name': database,
}

POSTGRESQL = {
    'engine': 'postgresql',
    'username': user,
    'password': password,
    'host': host,
    'db_name': database,
}
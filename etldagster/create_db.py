import psycopg2
import configparser
from sqlalchemy import create_engine

config = configparser.ConfigParser()
config.read('pg.cfg')

def create_database():
    """Create the database and connects to it
    """
    engine = create_engine("postgresql://{}:{}@{}:{}/{}".format(*config['DB'].values()))
    conn = engine.connect()
    conn.execute("commit")

    conn.execute("DROP DATABASE IF EXISTS matrizdb;")
    conn.execute("commit")
    conn.execute("CREATE DATABASE matrizdb WITH ENCODING 'utf8' TEMPLATE template0")
    conn.execute("commit")
    conn.close()

    engine = create_engine("postgresql://{}:{}@{}:{}/{}".format(*config['MATRIZ'].values()))
    conn = engine.connect()
    conn.execute("commit")

    return conn

def drop_table(conn):
    """Drop table in etldb
    """
    query1 = "DROP TABLE IF EXISTS matrizinfo;"
    conn.execute(query1)
    conn.execute("commit")

def create_table(conn):
    """create table in etldb
    """
    query = "CREATE TABLE IF NOT EXISTS matrizinfo(row VARCHAR(10), col VARCHAR(10), val INT PRIMARY KEY (row, col));"
    try:
        conn.execute(query)
        conn.execute("commit")
    except Exception as e:
        print(e)

# def main():
    # cur, conn = create_database()

    # drop_table(cur, conn)
    # create_table(cur, conn)
    # conn.close()

# if __name__ == "__main__":
#     main()
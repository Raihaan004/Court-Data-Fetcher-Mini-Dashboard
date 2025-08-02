import sqlite3
from sqlite3 import Error

def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect('queries.db')
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn):
    """ create a table to log queries """
    try:
        sql_create_table = """ CREATE TABLE IF NOT EXISTS queries (
                                        id integer PRIMARY KEY,
                                        case_type text NOT NULL,
                                        case_number text NOT NULL,
                                        case_year text NOT NULL,
                                        query_timestamp text NOT NULL,
                                        raw_response text
                                    ); """
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)

def log_query(conn, query_details):
    """
    Log a new query into the queries table
    """
    sql = ''' INSERT INTO queries(case_type,case_number,case_year,query_timestamp,raw_response)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, query_details)
    conn.commit()
    return cur.lastrowid
from datetime import datetime
from bank import conn, login_manager
from flask_login import UserMixin
from psycopg2 import sql


@login_manager.user_loader
def load_user(user_id):
    # TODO: Fix
    cur = conn.cursor()

    schema = 'customers'
    id = 'cpr_number'
    if str(user_id).startswith('60'):
        schema = 'employees'
        id = 'id'

    user_sql = sql.SQL("""
    SELECT * FROM {}
    WHERE {} = %s
    """).format(sql.Identifier(schema),  sql.Identifier(id))

    cur.execute(user_sql, (int(user_id),))
    if cur.rowcount > 0:
        return None


class User():
    def __init__(self):
        self.ID = 1 + 1 + 1


def insert_user(name):
    # TODO: Make functions for all SQL operations.
    cur = conn.cursor()
    sql = """
    INSERT INTO User(name)
    VALUES (%s)
    """
    cur.execute(sql, (name, CPR_number, password))
    conn.commit()
    cur.close()

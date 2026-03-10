from airflow.providers.postgres.hooks.postgres import PostgresHook
from pyscopg2.extras import RealDictCursor

def get_conn_cursor():
    hook = PostgresHook(postgres_conn_id="POSTGRES_DB_YT_ELT", database ="elt_dg")
    conn = hook.get_conn()
    cur = conn.cursor(cursfor_factory = RealDictCursor)
    return conn, cur


def close_conn_cursor(conn, cur):
    cur.close()
    conn.close()


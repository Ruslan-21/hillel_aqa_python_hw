import os
import psycopg2
import pytest

@pytest.fixture
def get_connection():
    host = os.getenv("HOST", "localhost")
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="test_password",
        host=host,
        port=5432
    )
    yield conn
    conn.close()

@pytest.fixture
def get_cursor(get_connection):
    cur = get_connection.cursor()
    yield cur
    cur.close()
    get_connection.commit()

def test_can_connect(get_connection):
    assert get_connection is not None

def test_table_crud(get_cursor):

    get_cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, name TEXT);")


    get_cursor.execute("INSERT INTO test_table (name) VALUES (%s) RETURNING id;", ("test_name",))
    inserted_id = get_cursor.fetchone()[0]
    assert inserted_id is not None

    get_cursor.execute("SELECT name FROM test_table WHERE id = %s;", (inserted_id,))
    name = get_cursor.fetchone()[0]
    assert name == "test_name"

    get_cursor.execute("UPDATE test_table SET name = %s WHERE id = %s;", ("updated_name", inserted_id))
    get_cursor.execute("SELECT name FROM test_table WHERE id = %s;", (inserted_id,))
    updated_name = get_cursor.fetchone()[0]
    assert updated_name == "updated_name"

    get_cursor.execute("DELETE FROM test_table WHERE id = %s;", (inserted_id,))
    get_cursor.execute("SELECT COUNT(*) FROM test_table WHERE id = %s;", (inserted_id,))
    count = get_cursor.fetchone()[0]
    assert count == 0

    get_cursor.execute("DROP TABLE test_table;")


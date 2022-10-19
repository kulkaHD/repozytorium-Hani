import sqlite3
from sqlite3 import Error


def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_connection_in_memory():

    conn = None
    try:
        conn = sqlite3.connect(":memory:")
        print(f"Connected, sqlite version: {sqlite3.version}")
    except Error as e:
       print(e)
    finally:
        if conn:
            conn.close()

def execute_sql(conn, sql):

    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)


def add_glos(conn, glos):

    sql = '''INSERT INTO glosy(partia, liczba_osob, sposob_wykonania)
             VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, glos)
    conn.commit()
    return cur.lastrowid

def add_chorzysta(conn, chorzysta):

    sql = '''INSERT INTO chorzysci(glos_id, imie, znajomosc_nut, czy_ma_spiewnik)
             VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, chorzysta)
    conn.commit()
    return cur.lastrowid

def update(conn, table, id, **kwargs):

    parameters = [f"{k} = ?" for k in kwargs]
    parameters = ", ".join(parameters)
    values = tuple(v for v in kwargs.values())
    values += (id, )

    sql = f''' UPDATE {table}
             SET {parameters}
             WHERE id = ?'''
    try:
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        print("OK")
    except sqlite3.OperationalError as e:
        print(e)

def delete_where(conn, table, **kwargs):

    qs = []
    values = tuple()
    for k, v in kwargs.items():
        qs.append(f"{k}=?")
        values += (v,)
    q = " AND ".join(qs)

    sql = f'DELETE FROM {table} WHERE {q}'
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()
    print("Deleted")

def delete_all(conn, table):

    sql = f'DELETE FROM {table}'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    print("Deleted")

if __name__ == "__main__":
    create_connection("chor_parafialny.db")
    create_connection_in_memory()
    conn = create_connection("chor_parafialny.db")
    
    create_glosy_sql = """
    -- glosy table
    CREATE TABLE IF NOT EXISTS glosy (
        id integer PRIMARY KEY,
        partia text NOT NULL,
        liczba_osob VARCHAR(15) NOT NULL,
        sposob_wykonania text NOT NULL
    );
    """
    create_chorzysci_sql = """
    -- chorzysci table
    CREATE TABLE IF NOT EXISTS chorzysci (
        id integer PRIMARY KEY,
        glos_id integer NOT NULL,
        imie text NOT NULL,
        znajomosc_nut VARCHAR(15) NOT NULL,
        czy_ma_spiewnik VARCHAR(15) NOT NULL,
        FOREIGN KEY (glos_id) REFERENCES glosy (id)
    );
    """

    execute_sql(conn, create_glosy_sql)
    execute_sql(conn, create_chorzysci_sql)

    glos1 = ("Sopran", "5", "głos")
    glos2 = ("Alt", "2", "głos")
    glos3 = ("Tenor", "1", "wiolonczela")
    glos4 = ("Bas", "1", "głos")
    
    gl1_id = add_glos(conn, glos1)
    gl2_id = add_glos(conn, glos2)
    gl3_id = add_glos(conn, glos3)
    gl4_id = add_glos(conn, glos4)

    chorzysta1 = (
        gl1_id,
        "Asia",
        "nie",
        "tak",
        )

    chorzysta2 = (
        gl2_id,
        "Martyna",
        "nie",
        "nie",
        )

    chorzysta3 = (
        gl3_id,
        "Hania",
        "tak",
        "tak",
        )

    chorzysta4 = (
        gl1_id,
        "Kasia",
        "tak",
        "tak",
        )

    chorzysta1_id = add_chorzysta(conn, chorzysta1)
    chorzysta2_id = add_chorzysta(conn, chorzysta2)
    chorzysta3_id = add_chorzysta(conn, chorzysta3)
    chorzysta4_id = add_chorzysta(conn, chorzysta4)
    
    update(conn, "glosy", 2, liczba_osob ="3")
    update(conn, "chorzysci", 2, czy_ma_spiewnik ="tak")

    delete_where(conn, "chorzysci", id=3)
    # delete_all(conn, "chorzysci")
    # delete_all(conn, "glosy")
    conn.close()
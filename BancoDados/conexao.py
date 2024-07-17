import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / "diobank.sqlite")

cursor = con.cursor()


def criar_tabela(con, cursor):
    cursor.execute(
        'CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')


def criar_registro(con, cursor, nome, email):
    data = (nome, email)

    cursor.execute(
        "INSERT INTO clientes (nome, email) VALUES (?, ?);", data)

    con.commit()


def atualizar_registro(con, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    con.commit()


def excluir_registro(con, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    con.commit()


def inserir_registros(con, cursor, dados):
    cursor.executemany(
        "INSERT INTO clientes (nome, email) VALUES (?, ?);", dados)
    con.commit()


def buscar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?;", (id,))
    return cursor.fetchone()


def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes;")

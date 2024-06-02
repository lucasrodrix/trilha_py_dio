import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "banco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute("DELETE FROM clientes WHERE id = 9;")
    conexao.commit()

    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?)", ("Noah Barbosa", "noahbarbosa@gruporodrix.net"))
    cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?,?,?)", (2, "Henry Rodrigues", "henryrodrix@gruporodrix.net"))
    conexao.commit()
except Exception as exc:
    print(f"Ops! um erro ocorreu! {exc}")
    conexao.rollback()
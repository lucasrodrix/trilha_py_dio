import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH/'banco.sqlite')
cursor = conn.cursor()
cursor.row_factory = sqlite3.Row

def create(self, cursor):
    cursor.execute("create table clientes(id integer primary key autoincrement, nome varchar(100),email varchar(150))")
    conn.commit()

def insert(conn, cursor, nome, email):
    data = (nome, email)
    cursor.execute("insert into clientes(nome,email) values(?,?);",data)
    conn.commit()

def update(conn, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("update clientes set nome=?, email=? where id=?;",data)
    conn.commit()

def delete(conn, cursor, id):
    data = (id,)
    cursor.execute("delete from clientes where id=?; ",data)
    conn.commit()

def insertMany(conn, cursor, datas):
    cursor.executemany("insert into clientes(nome,email) values(?,?);", datas)
    conn.commit()

# insert(conn, cursor, "Lucas Rodrigues","lucasrodrix@gruporodrix.net")
# insert(conn, cursor, "Andreas Barbosa","andreasbarbosa@gruporodrix.net")
# insert(conn, cursor, "Samuel Rodrigues","samuelrodrix@gruporodrix.net")
# update(conn, cursor, "Sarah Rodrigues","sarahrodrix@gruporodrix.net",1)
# delete(conn, cursor, 4)

# datas = [('Daisy Rodrix','daisyrodrix@gruporodrix'),('Alice Freitas Rodrigues','alicerodrix@gruporodrix.net')]
# insertMany(conn, cursor, datas)

def show_clients(cursor, id):
    cursor.execute('select id, email from clientes where id=?',(id,))
    return cursor.fetchone()

cliente = show_clients(cursor, 1)
print(cliente)

def show_list(cursor):
    return cursor.execute('select * from clientes order by nome;')

clientes = show_list(cursor)
# print(cliente) #Retorna um iteravel
for cliente in clientes:
    print(dict(cliente))

print(f'Seja Bem-Vindo(a) ao Sistema {cliente['nome']}')
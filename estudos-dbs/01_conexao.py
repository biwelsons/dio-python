import sqlite3
import pandas as pd

con = sqlite3.connect("clients.sqlite")

cur = con.cursor()

def criarTabela(con, cur):
    cur.execute(
        "CREATE TABLE clients (id INTEGER PRYMARY KEY AUTO INCREMENT, nome VARCHAR(255), email VARCHAR(255))"
        )
    con.commit()

def inserirRegistro(name: str, email: str):
    
    data = (name, email)

    cur.execute("INSERT INTO clients (nome, email) VALUES (?,?)", data)

    con.commit()

def listarRegistros():
    
    data = cur.execute("SELECT * FROM clients ")
    df_data = pd.DataFrame(data)
    return df_data

def limparRegistros(id=None):
    
    if id is None:
        cur.execute("DELETE FROM clients")
    else:
        cur.execute("DELETE FROM client WHERE id = %s", id)
    con.commit()


inserirRegistro('gabs', 'gabs@email.com')
print(listarRegistros())
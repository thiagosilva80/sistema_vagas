import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Theus@819",
        database="sistemas_vagas"
    )
from database.conexao import conectar

def cadastrar_usuario(nome_usuario, email_usuario, senha_usuario):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO tbl_usuarios(nome_usuario, email_usuario, senha_usuario)
    VALUES (%s,%s,%s)
    """
    
    valores = (nome_usuario, email_usuario, senha_usuario)

    cursor.execute(sql, valores)
    conexao.commit()

    print("Usuario cadastrado com sucesso!")

    cursor.close()
    conexao.close()

def login(email_usuario, senha_usuario):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT * FROM tbl_usuarios
    WHERE email_usuario = %s AND senha_usuario = %s
    """

    cursor.execute(sql, (email_usuario, senha_usuario))

    usuario = cursor.fetchone()
    
    cursor.close()
    conexao.close()

    return usuario
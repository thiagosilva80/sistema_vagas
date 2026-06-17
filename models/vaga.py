from database.conexao import conectar

def cadastrar_vaga(titulo_vagas, empresa_vagas, descricao_vagas):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO tbl_vagas (titulo_vagas, empresa_vagas, descricao_vagas)
    VALUES (%s, %s, %s)
    """
    print(sql)
    print(titulo_vagas)
    print(empresa_vagas)
    print(descricao_vagas)

    cursor.execute(sql, (titulo_vagas, empresa_vagas, descricao_vagas))

    conexao.commit()

    print("Vaga cadastrada!")

    cursor.close()
    conexao.close()

def listar_vagas():
    conexao = conectar()
    cursor = conexao.cursor()

    
    cursor.execute("SELECT * FROM tbl_vagas")

    vagas = cursor.fetchall()

    cursor.close()
    conexao.close()

    return vagas
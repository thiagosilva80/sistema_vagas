from database.conexao import conectar

def candidatar(usuario_id, vaga_id):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO candidaturas(usuario_id, vaga_id)
    VALUES (%s, %s)
    """

    cursor.execute(sql, (usuario_id, vaga_id))

    conexao.commit()

    print("Candidatura realizada!")

    cursor.close()
    conexao.close()

def minhas_candidaturas(usuario_id):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT vagas.titulo
    FROM candidaturas
    INNER JOIN vagas
    ON vagas.id = candidaturas.vaga_id
    WHERE candidaturas.usuario_id = %s
    """

    cursor.execute(sql, (usuario_id,))

    vagas = cursor.fetchall()

    cursor.close()
    conexao.close()

    return vagas
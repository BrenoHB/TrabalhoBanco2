import psycopg2

# Função para conectar ao banco PostgreSQL
def conectar_postgres():
    return psycopg2.connect(
        dbname="trabalhobanco",     # troque pelo nome do seu banco
        user="postgres",       # seu usuário
        password="unochapeco",      # sua senha
        host="localhost",      # ou o IP do servidor
        port="5432"
    )

# CREATE
def criar_usuario(nome, email):
    conn = conectar_postgres()
    cur = conn.cursor()
    cur.execute("INSERT INTO usuarios (nome, email) VALUES (%s, %s)", (nome, email))
    conn.commit()
    cur.close()
    conn.close()

# READ
def listar_usuarios():
    conn = conectar_postgres()
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuarios")
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    return resultado

# UPDATE
def atualizar_usuario(nome_antigo, novo_email):
    conn = conectar_postgres()
    cur = conn.cursor()
    cur.execute("UPDATE usuarios SET email = %s WHERE nome = %s", (novo_email, nome_antigo))
    conn.commit()
    cur.close()
    conn.close()

# DELETE
def deletar_usuario(nome):
    conn = conectar_postgres()
    cur = conn.cursor()
    cur.execute("DELETE FROM usuarios WHERE nome = %s", (nome,))
    conn.commit()
    cur.close()
    conn.close()

# app.py
import psycopg2
import redis

# ===== PostgreSQL Utils =====
def conectar_postgres():
    return psycopg2.connect(
        dbname="trabalhobanco",  # seu banco
        user="postgres",          # seu usuário
        password="unochapeco",    # sua senha
        host="localhost",
        port="5432"
    )

def criar_usuario(nome, email):
    conn = conectar_postgres()
    cur = conn.cursor()
    cur.execute("INSERT INTO usuarios (nome, email) VALUES (%s, %s)", (nome, email))
    conn.commit()
    cur.close()
    conn.close()
    print("Usuário criado com sucesso!")

def listar_usuarios():
    conn = conectar_postgres()
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuarios")
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    return resultado

def atualizar_usuario(nome_antigo, novo_email):
    conn = conectar_postgres()
    cur = conn.cursor()
    cur.execute("UPDATE usuarios SET email = %s WHERE nome = %s", (novo_email, nome_antigo))
    conn.commit()
    cur.close()
    conn.close()
    print("Usuário atualizado com sucesso!")

def deletar_usuario(nome):
    conn = conectar_postgres()
    cur = conn.cursor()
    cur.execute("DELETE FROM usuarios WHERE nome = %s", (nome,))
    conn.commit()
    cur.close()
    conn.close()
    print("Usuário deletado com sucesso!")

# ===== Redis Utils =====
def conectar_redis():
    return redis.Redis(host='localhost', port=6379, db=0)

def testar_redis():
    r = conectar_redis()
    r.set("teste", "Olá Redis!")
    print("Valor em Redis:", r.get("teste").decode())

# ===== Menu =====
def menu():
    while True:
        print("\n==== MENU CRUD ====")
        print("1 - Criar usuário")
        print("2 - Listar usuários")
        print("3 - Atualizar usuário")
        print("4 - Deletar usuário")
        print("5 - Testar Redis")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            criar_usuario(nome, email)
        elif opcao == "2":
            usuarios = listar_usuarios()
            if usuarios:
                print("Usuários cadastrados:")
                for u in usuarios:
                    print(f"ID: {u[0]}, Nome: {u[1]}, Email: {u[2]}")
            else:
                print("Nenhum usuário encontrado.")
        elif opcao == "3":
            nome_antigo = input("Nome do usuário a atualizar: ")
            novo_email = input("Novo email: ")
            atualizar_usuario(nome_antigo, novo_email)
        elif opcao == "4":
            nome = input("Nome do usuário a deletar: ")
            deletar_usuario(nome)
        elif opcao == "5":
            testar_redis()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# ===== Criação da tabela inicial =====
def criar_tabela():
    conn = conectar_postgres()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

# ===== MAIN =====
if __name__ == "__main__":
    criar_tabela()
    menu()

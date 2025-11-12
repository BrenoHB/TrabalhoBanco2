import redis

# Conexão com o Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# CREATE
def criar_usuario(chave, valor):
    r.set(chave, valor)

# READ
def ler_usuario(chave):
    return r.get(chave)

# UPDATE
def atualizar_usuario(chave, novo_valor):
    r.set(chave, novo_valor)

# DELETE
def deletar_usuario(chave):
    r.delete(chave)

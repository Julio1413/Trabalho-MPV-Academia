import json,os
from ..config import ARQUIVO_USUARIO

class Usuario:
    def __init__(self,
            nome=None,
            matricula=None):
        self.nome = nome
        self.matricula = matricula



usuario = Usuario()
    
def CarregarUsuario():
    global usuario
    with open(os.path.join(ARQUIVO_USUARIO)) as f:
        info = json.loads(f.read())
    try:
        usuario.nome = info['nome']
        usuario.matricula = info['matricula']
        return {'nome':usuario.nome, 'matricula':usuario.matricula}
    except:
        return None

def SalvarUsuario(nome_novo:None, matricula_nova=None):
    global usuario
    with open(os.path.join(ARQUIVO_USUARIO),"w") as f:
        f.write(json.dumps({"nome":{nome_novo},"matricula":{matricula_nova}}))

    usuario.matricula =matricula_nova
    usuario.nome = nome_novo
    
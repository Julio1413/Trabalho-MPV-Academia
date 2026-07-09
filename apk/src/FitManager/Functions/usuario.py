import json
import os
from ..config import ARQUIVO_USUARIO, JSON_USUARIOS


class Usuario:
    def __init__(self, nome=None, matricula=None):
        self.nome = nome
        self.matricula = matricula


usuario = Usuario()


def CarregarUsuario():
    global usuario

    if not os.path.exists(ARQUIVO_USUARIO):
        return None

    with open(ARQUIVO_USUARIO, "r", encoding="utf-8") as f:
        conteudo = f.read().strip()

    if not conteudo:
        return None

    try:
        info = json.loads(conteudo)

        usuario.nome = info["nome"]
        usuario.matricula = info["matricula"]

        return {
            "nome": usuario.nome,
            "matricula": usuario.matricula
        }
    except (KeyError, json.JSONDecodeError):
        return None


def SalvarUsuario(nome_novo=None, matricula_nova=None):
    global usuario

    with open(ARQUIVO_USUARIO, "w", encoding="utf-8") as f:
        json.dump(
            {
                "nome": nome_novo,
                "matricula": matricula_nova
            },
            f,
            ensure_ascii=False,
            indent=4
        )

    usuario.nome = nome_novo
    usuario.matricula = matricula_nova


def CarregarTodos():
    if not os.path.exists(JSON_USUARIOS):
        return []

    with open(JSON_USUARIOS, "r", encoding="utf-8") as f:
        conteudo = f.read().strip()

    if not conteudo:
        return []

    try:
        return json.loads(conteudo)
    except json.JSONDecodeError:
        return []


def CriarUsuario(nome, matricula):
    global usuario

    usuario.nome = nome
    usuario.matricula = matricula

    lista_usuarios = CarregarTodos()

    lista_usuarios.append({
        "nome": nome,
        "matricula": matricula
    })

    with open(JSON_USUARIOS, "w", encoding="utf-8") as f:
        json.dump(
            lista_usuarios,
            f,
            ensure_ascii=False,
            indent=4
        )

    SalvarUsuario(nome_novo=nome, matricula_nova=matricula)
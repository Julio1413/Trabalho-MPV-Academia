import flet as ft
from pathlib import Path
import os
from FitManager.pages import login,inicial
from FitManager.Functions import usuario
from FitManager.config import PASTA_TREINOS, PASTA_USUARIOS, ARQUIVO_USUARIO,JSON_USUARIOS,ARQUIVO_LISTA_TREINOS

#Gerenciamento de login
IR_PARA_LOGIN = None

#Forçar a existência dos arquivos
if not os.path.exists(os.path.join(PASTA_USUARIOS)):
    PASTA_USUARIOS.mkdir(exist_ok=True)
if not os.path.exists(os.path.join(PASTA_TREINOS)):
    PASTA_TREINOS.mkdir(exist_ok=True)



if not os.path.exists(os.path.join(ARQUIVO_LISTA_TREINOS)):
    with open(os.path.join(ARQUIVO_LISTA_TREINOS),'w') as f:
        f.write('[]')
if not os.path.exists(os.path.join(ARQUIVO_USUARIO)):
    with open(os.path.join(ARQUIVO_USUARIO),'w') as f:
        f.write('[]')
    IR_PARA_LOGIN =True
if not os.path.exists(os.path.join(JSON_USUARIOS)):
    with open(os.path.join(JSON_USUARIOS),'w') as f:
        f.write('[]')
    IR_PARA_LOGIN = True


#Verifica a existência do usuario
info_usuario = usuario.CarregarUsuario()

def main(page:ft.Page):
    page.title="FitManager"
    page.bgcolor = ft.Colors.PURPLE_900

    if not info_usuario or IR_PARA_LOGIN:login.login(page)
    else:inicial.home(page)
   




ft.app(main)
import flet as ft
from pathlib import Path
import os, platform
from FitManager.pages import login,inicial
from FitManager.Functions import usuario
from FitManager.config import  PASTA_USUARIOS, ARQUIVO_USUARIO,JSON_USUARIOS
from FitManager import config

#Gerenciamento de login
IR_PARA_LOGIN = None

#Forçar a existência dos arquivos
if not os.path.exists(os.path.join(PASTA_USUARIOS)):
    PASTA_USUARIOS.mkdir(exist_ok=True)



if not os.path.exists(os.path.join(ARQUIVO_USUARIO)):
    with open(os.path.join(ARQUIVO_USUARIO),'w') as f:
        f.write('')
    IR_PARA_LOGIN =True
if not os.path.exists(os.path.join(JSON_USUARIOS)):
    with open(os.path.join(JSON_USUARIOS),'w') as f:
        f.write('')
    IR_PARA_LOGIN = True


#Verifica a existência do usuario
info_usuario = usuario.CarregarUsuario()

async def main(page:ft.Page):
    page.title="FitManager"
    page.bgcolor = ft.Colors.PURPLE_900
    page.theme_mode =ft.ThemeMode.DARK

    #Pasta global
    sistema = platform.system()
    # Windows
    if sistema == "Windows":
        config.PASTA_GLOBAL = (Path(__file__).resolve().parent.parent) 
        os.makedirs(config.PASTA_GLOBAL, exist_ok=True)
        
    # Android
    elif "ANDROID_BOOTLOGO" in os.environ or (sistema == "Linux" and "arm" in platform.uname().machine):
        storage = ft.StoragePaths()
        config.PASTA_GLOBAL = await storage.get_application_support_directory()

    # Linux comum
    elif sistema == "Linux":
        config.PASTA_GLOBAL = (Path(__file__).resolve().parent.parent) 
        os.makedirs(config.PASTA_GLOBAL, exist_ok=True)

    if not info_usuario or IR_PARA_LOGIN:login.login(page)
    else:inicial.home(page)
   




ft.app(main)
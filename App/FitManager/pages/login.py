import flet as ft
from ..Functions import ui_tools

def login (page):
    page.title = 'Login - FitManager'
    page.update
    page.add(ui_tools.header(page=page,icone_direita=ft.Icons.LOGIN_ROUNDED,texto='Login FitManager', icone_esquerda=ft.Icons.FITNESS_CENTER_ROUNDED))
    page.add(ui_tools.container(page=page,controles=[ft.Text('Teste')]))
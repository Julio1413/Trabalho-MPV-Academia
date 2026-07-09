from enum import nonmember
import flet as ft
from ..Functions import ui_tools,usuario
from ..pages import inicial

def login_novo_usuario(page):
    page.clean()
    def criar_conta(nome,matricula):
        if not nome or not matricula: 
            page.show_dialog(ft.SnackBar(ft.Text('Preencha ambos os campos!'),bgcolor=ft.Colors.RED))
            return
        usuario.CriarUsuario(nome=nome,matricula=matricula)
        inicial.home(page)
    
    #Entradas
    nome_input  = ft.TextField(label="Nome",border_color=page.bgcolor,width=page.width,border_radius=30,keyboard_type=ft.KeyboardType.NAME)
    matricula_input = ft.TextField(label="Matrícula",border_color=page.bgcolor,width=page.width,border_radius=30,keyboard_type=ft.KeyboardType.NUMBER)

    #Botoes

    cadastro_botao = ft.ElevatedButton(content=ft.Text("Cadastrar-se",color=ft.Colors.WHITE),bgcolor=page.bgcolor,width=page.width,height=50,on_click=lambda _:criar_conta(nome=nome_input.value,matricula=matricula_input.value))

    page.add(ui_tools.header(page=page,icone_direita=ft.Icons.LOGIN_ROUNDED,texto='Criar Conta', icone_esquerda=ft.Icons.FITNESS_CENTER_ROUNDED))
    page.add(ft.Placeholder(color=ft.Colors.TRANSPARENT,height=7))


    page.add(ui_tools.container(page=page,controles=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                            ft.Image(src='https://i.ibb.co/27F5FZgS/login.png',fit=ft.BoxFit.COVER,width=page.width*0.4),
                        ]
                    ),


                nome_input ,
                matricula_input,
                cadastro_botao,
            ]   
        )
    )


def login (page):
    page.title = 'Login - FitManager'
    page.update

    def verificar_efetuar_login(nome, matricula):
        home = False
        if not nome or not matricula: 
            page.show_dialog(ft.SnackBar(ft.Text('Preencha ambos os campos!'),bgcolor=ft.Colors.RED))
            return
        for pessoa in usuario.CarregarTodos():
            if nome ==pessoa['nome'] and matricula == pessoa['matricula']:
                usuario.SalvarUsuario(nome_novo=nome,matricula_nova=matricula)
                page.show_dialog(ft.SnackBar(ft.Text('Login efetuado com sucesso!'),bgcolor=ft.Colors.GREEN))
                inicial.home(page)
                home=True
                break
        if home ==False:page.show_dialog(ft.SnackBar(ft.Text('Conta não encontrada, efetue a criação da sua conta FitManager!'),bgcolor=ft.Colors.RED))

        




    #Entradas
    nome_input  = ft.TextField(label="Nome",border_color=page.bgcolor,width=page.width,border_radius=30,keyboard_type=ft.KeyboardType.NAME)
    matricula_input = ft.TextField(label="Matrícula",border_color=page.bgcolor,width=page.width,border_radius=30,keyboard_type=ft.KeyboardType.NUMBER)

    #Botoes

    entrar_botao = ft.ElevatedButton(content=ft.Text('Entrar',color=ft.Colors.WHITE),bgcolor=page.bgcolor,width=page.width,height=50,on_click=lambda _:verificar_efetuar_login(nome=nome_input.value,matricula=matricula_input.value))
    cadastro_botao = ft.ElevatedButton(content=ft.Text("Cadastrar-se",color=ft.Colors.WHITE),bgcolor=page.bgcolor,width=page.width,height=50,on_click=lambda _:login_novo_usuario(page))

    page.add(ui_tools.header(page=page,icone_direita=ft.Icons.LOGIN_ROUNDED,texto='Login FitManager', icone_esquerda=ft.Icons.FITNESS_CENTER_ROUNDED))
    page.add(ft.Placeholder(color=ft.Colors.TRANSPARENT,height=7))


    page.add(ui_tools.container(page=page,controles=[

                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                            ft.Image(src='https://i.ibb.co/27F5FZgS/login.png',fit=ft.BoxFit.COVER,width=page.width*0.4),
                        ]
                    ),


                nome_input ,
                matricula_input,
                entrar_botao,
                cadastro_botao,
            ]   
        )
    )
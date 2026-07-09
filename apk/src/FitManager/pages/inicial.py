import flet as ft
from ..Functions import ui_tools,usuario
from ..pages import treino

def home(page):
    page.clean()
    page.title='Home - FitManager'
    page.add(ui_tools.header(
        page=page,
        texto='Início',
        icone_direita=ft.Icons.HOME_ROUNDED,
        icone_esquerda=ft.Icons.FITNESS_CENTER_ROUNDED
    ))

    page.add(
        ft.Container(
            bgcolor=ft.Colors.BLACK,
            width=page.width,
            border_radius=35,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                controls=[
                    ft.Icon(icon=ft.Icons.PERSON,size=80,color=ft.Colors.WHITE),
                    ft.Column(
                        [
                            ft.Text(f'{usuario.usuario.nome}',weight=ft.FontWeight.BOLD),
                            ft.Text(f'{usuario.usuario.matricula}',weight=ft.FontWeight.BOLD)
                        ]
                    )
                ]
            )
        )
    )
    page.add(
        ft.Container(
            expand=True,
            padding=10,
            bgcolor=ft.Colors.BLACK,
            border_radius=35,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.START,
                scroll=ft.ScrollMode.AUTO,
                expand=True,
                spacing=5,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        controls=[
                            ft.Image(src='https://i.ibb.co/23kQFzhP/IMG-20260709-WA0004.jpg',fit=ft.BoxFit.FILL,width=page.width*0.08,height=page.width*0.08),
                            ft.Text('FitManager',weight=ft.FontWeight.BOLD),
                            ft.Icon(icon=ft.Icons.CIRCLE,color=ft.Colors.TRANSPARENT)
                        ]
                    ),
                    ft.Divider(),
                    #Botões
                    ft.Container(
                        on_click=lambda _:treino.pagina_treinos(page),
                        height=30,width=page.width,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            controls=[
                                ft.Icon(icon=ft.Icons.FITNESS_CENTER_ROUNDED,size=25),
                                ft.Text('Lista de treinos',weight=ft.FontWeight.BOLD),
                                ft.Icon(icon=ft.Icons.FIT_SCREEN_ROUNDED,color=ft.Colors.TRANSPARENT,size=25),
                            ]
                        )
                    )
                ]
            )
        )
    )
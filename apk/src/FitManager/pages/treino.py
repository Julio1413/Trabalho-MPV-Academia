import flet as ft
from ..pages import inicial
from ..Functions import ui_tools
TREINOS_FIXOS = {
    "Treino A": [
        {"Nome": "Supino reto", "Series": 4, "Repeticoes": 10},
        {"Nome": "Supino inclinado", "Series": 4, "Repeticoes": 12},
        {"Nome": "Crucifixo", "Series": 3, "Repeticoes": 12},
        {"Nome": "Rosca direta", "Series": 3, "Repeticoes": 10},
        {"Nome": "Rosca alternada", "Series": 3, "Repeticoes": 12},
    ],
    "Treino B": [
        {"Nome": "Puxada frontal", "Series": 4, "Repeticoes": 10},
        {"Nome": "Remada curvada", "Series": 4, "Repeticoes": 10},
        {"Nome": "Remada baixa", "Series": 3, "Repeticoes": 12},
        {"Nome": "Triceps testa", "Series": 3, "Repeticoes": 10},
        {"Nome": "Triceps corda", "Series": 3, "Repeticoes": 12},
    ],
    "Treino C": [
        {"Nome": "Agachamento livre", "Series": 4, "Repeticoes": 10},
        {"Nome": "Leg press", "Series": 4, "Repeticoes": 12},
        {"Nome": "Cadeira extensora", "Series": 3, "Repeticoes": 15},
        {"Nome": "Afundo", "Series": 3, "Repeticoes": 12},
        {"Nome": "Panturrilha em pe", "Series": 4, "Repeticoes": 20},
    ],
    "Treino D": [
        {"Nome": "Stiff", "Series": 4, "Repeticoes": 10},
        {"Nome": "Mesa flexora", "Series": 4, "Repeticoes": 12},
        {"Nome": "Elevacao pelvica", "Series": 4, "Repeticoes": 12},
        {"Nome": "Abdutora", "Series": 3, "Repeticoes": 15},
        {"Nome": "Panturrilha sentado", "Series": 4, "Repeticoes": 20},
    ],
}


def treino_especifico(page, nome_treino, treino=None):
    page.clean()
    treino = treino or []

    controles_treino = []
    controles_treino.append(
        ft.Row(
            width=page.width,
            height=60,
            margin=-10,
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.IconButton(
                    icon=ft.Icons.ARROW_BACK_IOS_ROUNDED,
                    icon_color=ft.Colors.WHITE,
                    on_click=lambda _: pagina_treinos(page),
                ),
                ft.Text(value=nome_treino, weight=ft.FontWeight.BOLD, size=17),
                ft.Icon(icon=ft.Icons.FITNESS_CENTER_ROUNDED),
            ],
        )
    )

    for exercicio in treino:
        controles_treino.append(
            ft.Container(
                bgcolor=ft.Colors.GREY_900,
                border_radius=20,
                padding=15,
                width=page.width,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Column(
                            spacing=3,
                            controls=[
                                ft.Text(
                                    exercicio["Nome"],
                                    weight=ft.FontWeight.BOLD,
                                    size=16,
                                ),
                                ft.Text(
                                    f'{exercicio["Series"]} séries x {exercicio["Repeticoes"]} repetições',
                                    size=13,
                                ),
                            ],
                        ),
                        ft.Icon(icon=ft.Icons.CHECK_CIRCLE_OUTLINE_ROUNDED),
                    ],
                ),
            )
        )

    page.add(
        ui_tools.container(
            page=page,
            controles=controles_treino,
        )
    )
    page.update()

def pagina_treinos (page):
    page.clean()
    page.add(
        ft.Row(
        width=page.width,
        height=60,
        margin=-10,
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        controls=[
            ft.IconButton(icon=ft.Icons.ARROW_BACK_IOS_ROUNDED,icon_color=ft.Colors.WHITE,on_click=lambda _:inicial.home(page)),
            ft.Text(value="Treinos",weight=ft.FontWeight.BOLD,size=17),
            ft.Icon(icon=ft.Icons.FITNESS_CENTER_ROUNDED),
            ]
        )
    )
    def botoes_treino(nome,categoria,imagem,destino):
        return ft.Container(
            bgcolor=ft.Colors.BLACK_26,
            border_radius=35,
            on_click=destino,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=
                [
                    ft.Image(src=imagem,fit=ft.BoxFit.FILL,width=page.width*0.3,height=page.width*0.3,border_radius=25),
                    ft.Column([
                        ft.Text(nome,weight=ft.FontWeight.BOLD),
                        ft.Text(categoria),
                        ]),
                    ft.Placeholder(color=ft.Colors.TRANSPARENT,width=page.width*0.05,height=1)
                ]
            )
        )
    page.add(
        ui_tools.container(page=page,
            controles=[
                botoes_treino(
                    'Treino A',
                    'Peitoral - Bíceps',
                    'https://i.ibb.co/zWZDn4Zw/peitoral.jpg',
                    lambda _: treino_especifico(page, 'Treino A', TREINOS_FIXOS['Treino A']),
                ),
                ft.Divider(),
                botoes_treino(
                    'Treino B',
                    'Costas - Tríceps',
                    'https://i.ibb.co/WNsNPfTL/costas.jpg',
                    lambda _: treino_especifico(page, 'Treino B', TREINOS_FIXOS['Treino B']),
                ),
                ft.Divider(),
                botoes_treino(
                    'Treino C',
                    'Coxa - Panturrilha',
                    'https://i.ibb.co/cXM0MrTp/coxa.jpg',
                    lambda _: treino_especifico(page, 'Treino C', TREINOS_FIXOS['Treino C']),
                ),
                ft.Divider(),
                botoes_treino(
                    'Treino D',
                    'Posterior - Panturrilha - \nGlúteo',
                    'https://i.ibb.co/YwLCg5H/posterior.png',
                    lambda _: treino_especifico(page, 'Treino D', TREINOS_FIXOS['Treino D']),
                ),
                ft.Divider(),
            ]
        )
    )

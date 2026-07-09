import flet as ft

def header(
    page,
    texto,
    icone_direita,
    icone_esquerda
):
    return ft.Row(
        width=page.width,
        height=60,
        margin=-10,
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        controls=[
            ft.Icon(icon=icone_direita),
            ft.Text(value=texto,weight=ft.FontWeight.BOLD,size=17),
            ft.Icon(icon=icone_esquerda),
            ]
        )
    
def container(page, controles):
    return ft.Container(
        padding=10,
        margin=-10,
        expand=True,
        width=page.width,
        bgcolor=ft.Colors.BLACK,
        border_radius=ft.BorderRadius.only(top_left=25,top_right=25),
        content=ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            controls=controles
        )
    )

import flet as ft


def main(page: ft.Page) -> None:
    page.title = "Flet Starter"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    name_field = ft.TextField(label="Your name", autofocus=True)
    greeting_text = ft.Text(value="Hello, Flet!", selectable=True)

    def handle_button_click(_):
        person_name = name_field.value.strip() or "Flet"
        greeting_text.value = f"Hello, {person_name}!"
        page.update()

    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "Welcome to Flet + Python",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                ),
                name_field,
                ft.ElevatedButton("Say hi", on_click=handle_button_click),
                greeting_text,
            ],
            width=400,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            tight=True,
            spacing=16,
        )
    )


if __name__ == "__main__":
    ft.app(target=main)


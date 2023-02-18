import flet as ft

def main(page: ft.Page):
    # setting up the page title
    page.title = "Enjoy MadLibs"
    page.theme_mode = "dark"
    page.horizontal_alignment = "center"
    page.padding = 40
    page.scroll = "always"

    # text inputs
    occupation = ft.TextField(hint_text="any occupation(job)...", border_radius=20)
    noun_01 = ft.TextField(hint_text="any noun...", border_radius=20)
    adj_01 = ft.TextField(hint_text="any adjective...", border_radius=20)
    noun_02 = ft.TextField(hint_text="any noun...", border_radius=20)
    verb_01 = ft.TextField(hint_text="any verb...", border_radius=20)
    adj_02 = ft.TextField(hint_text="any adjective...", border_radius=20)
    noun_03 = ft.TextField(hint_text="any noun...", border_radius=20)
    verb_02 = ft.TextField(hint_text="any verb...", border_radius=20)
    noun_04 = ft.TextField(hint_text="any noun...", border_radius=20)
    verb_03 = ft.TextField(hint_text="any verb...", border_radius=20)

    final_madlib = ft.Text(color="#FFFF00", font_family="SunnyspellsRegular-MV9ze", style="headlineLarge")

    # configuring the font
    page.fonts = {
        "charmelade": "fonts/charmelade.otf",
        "SunnyspellsRegular-MV9ze": "fonts/SunnyspellsRegular-MV9ze.otf"
    }

    # game title
    title = ft.Text("Enjoy MadLibs", font_family="charmelade", style="displayMedium", color="#FFFFFF")
    
    def generate_madlib(e):
        final_madlib.value = f"Today a {occupation.value} named {noun_04.value} came to our school to talk to us about her job. She said the most important skill you need to know to do her job is to be able to {verb_02.value} around (a) {adj_01.value} {noun_03.value}. She said it was easy for her to learn her job because she loved to {verb_01.value} when she was my age--and that helps a lot! If you're considering her profession, I hope you can be near (a) {adj_02.value} {noun_01.value}. That's very important! If you get too distracted in that situation you won't be able to {verb_03.value} next to (a) {noun_02.value}!"
        page.update()

    # adding components to the page
    page.add(
        title,
        ft.Row(),
        ft.Row(),
        ft.Row([occupation, noun_01], alignment="center"),
        ft.Row([adj_01, noun_02], alignment="center"),
        ft.Row([verb_01, adj_02], alignment="center"),
        ft.Row([noun_03, verb_02], alignment="center"),
        ft.Row([noun_04, verb_03], alignment="center"),
        ft.Row(),
        ft.Row(),
        ft.Text(value="Hint: a Verb is an action. A noun is a person/place/thing. An adjective describes a person/place/thing.", italic=True),
        ft.Row(),
        ft.Row(),
        ft.ElevatedButton("Generate MadLib", on_click=generate_madlib),
        ft.Row(),
        ft.Row(),
        final_madlib
    )

# calling the main function
ft.app(target=main, assets_dir="assets")
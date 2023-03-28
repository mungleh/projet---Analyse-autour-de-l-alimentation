# Import libraries nécessaires
from dash import html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO


template_theme1 = "bootstrap"
template_theme2 = "darkly"
url_theme1 = dbc.themes.BOOTSTRAP
url_theme2 = dbc.themes.DARKLY

# On defini ici la structure de la navbar
def Navbar():

    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Page 1", href="/page1")),
                dbc.NavItem(dbc.NavLink("Page 2", href="/page2")),
            ] ,
            brand="ANALYSE ALIMENTAIRE MONDIAL",
            brand_href="/",
            color="dark",
            dark=True,
        ),
    ])

    return layout

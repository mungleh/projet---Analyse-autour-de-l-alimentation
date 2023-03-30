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
                dbc.NavItem(dbc.NavLink("INPUT", href="/page1")),
            ] ,
            brand="ANALYSE ALIMENTAIRE MONDIAL",
            brand_href="/",
            color= '#5D7963',
            dark=True,
        ),
    ])

    return layout

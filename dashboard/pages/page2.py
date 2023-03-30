# Import libraries nécessaires
import dash
from dash import html
import dash_bootstrap_components as dbc

### On ajoute des composants
table_header = [
    html.Thead(html.Tr([html.Th("Prenom"), html.Th("Métiers")]))
]

row1 = html.Tr([html.Td("Alicia"), html.Td("Docteur")])
row2 = html.Tr([html.Td("Morgan"), html.Td("Chef de Projet")])
row3 = html.Tr([html.Td("Kams"), html.Td("euh...")])

table_body = [html.Tbody([row1, row2, row3])]

page2_table = dbc.Table(table_header + table_body, bordered=True)

# On defini le layout de la page 2
layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("Titre : Page 2")),
        html.Br(),
        html.Hr(),
        dbc.Col([
            html.P("Exemple column 1."),
            dbc.Button("Test Button", color="secondary")
        ]),
        dbc.Col([
            html.P("Exemple column 2."),
            page2_table
        ])
    ])
])

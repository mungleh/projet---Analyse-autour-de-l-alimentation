# Import libraries nécessaires
from dash import html, dcc, no_update
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from app import app
import plotly.express as px

aide = pd.read_csv("data/aide_alimentaire.csv", delimiter=",")
dispo = pd.read_csv("data/dispo_alimentaire.csv", delimiter=",")
pop = pd.read_csv("data/population.csv", delimiter=",")
inséc = pd.read_csv("data/sous_nutrition.csv", delimiter=",")


#On remplace par la date intervalle
insecurite = inséc.replace(['2012-2014', '2013-2015', '2014-2016', '2015-2017','2016-2018','2017-2019'],
                        ['2013', '2014', '2015', '2016','2017','2018'])
insecurite['Année'] = insecurite['Année'].astype('int64')

#supression des NaN
insecurite = insecurite.dropna()
sous_nutrition_pourcentage = insecurite["Valeur"].value_counts(normalize=True).mul(100).round(2).astype(str) + '%'



layout = html.Div([
    dcc.Dropdown(id='dropdown1',
                 options=[{'label':i, 'value':i} for i in pop['Année'].unique()]),
    dcc.Dropdown(id='dropdown2',
                 options=[{'label':i, 'value':i} for i in pop['Zone'].unique()]),
    dcc.Graph(id='graphic'),
    # html.Div(id='output-div')
])

@app.callback(
    Output('dropdown2', 'options'),
    [Input('dropdown1', 'value')])

def update_drop2(selected_drop):
    filtered_df = pop[(pop['Année'] == selected_drop)]
    return [{'label':i, 'value':i} for i in filtered_df['Zone'].unique()]


@app.callback(
Output('graphic', 'figure'),
[Input('dropdown1', 'value'), Input('dropdown2', 'value')])


# @app.callback(
#   Output('output-div', 'children'),
# Input('dropdown1', 'selected_value'))


def update_figure(selected_drop1, selected_drop2):

    if not selected_drop2:
        filtered_df = pop[(pop['Année'] == selected_drop1)]
    else:
        filtered_df = pop[(pop['Année'] == selected_drop1) &
                      (pop['Zone'] == selected_drop2)]
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=filtered_df.Valeur,y=filtered_df.Zone,
    marker = dict(size=15, color='green'), mode='markers'))

    return fig

# def update_output(selected_value):
#     insecurite_2017 =  insecurite.loc[insecurite['Année'] == selected_value]
#     pop_2017 = pop.loc[pop['Année'] == selected_value]
#     pop_mondial_2017 =  pop_2017['Valeur'].sum()/ 1e3
#     proportion_sous_nutrition = round((insecurite_2017["Valeur"].sum() / pop_mondial_2017) * 100, 2)
#     return html.Div('La proportion de la population en sous-nutrition en {} est de {}%'.format(selected_value, proportion_sous_nutrition))






# dropdown_col = [2016,2017]
# refresh = html.A(html.Button('Refresh df'),href='/')

# droplist = html.Div(
#     [
#     dcc.Dropdown(dropdown_col,id="dropdown" ,clearable=False,  className="m-3",value=2017,),

#     ]
# )

# output_container = html.Div()

# row_dropdown = dbc.Container(
#     [

#         html.Label("Selection de paramétres"),
#         droplist,
#         dcc.Loading(output_container),
#     ],
#     fluid=True,
# )


# #--------------------------------CallBack------------------------------#
# @app.callback(
#         Output('graph', 'figure'),
#         Input('dropdown', 'value'),
#         # Output("graph", "figure"),
#         # Input("names", "value"),
#         # Input("values", "value")
#     )

# #--------------------------------Function------------------------------#
# def update_output(value):
#     pop_2017 = pop.loc[pop['Année'] == value]
#     graph = px.histogram( pop_2017 , x="Valeur", nbins=10, title="Life Expectancy")
#     return graph

# def update_figure(selected_value):

#     if selected_value == 2017:

#          graph = px.histogram( pop_2017 , x="Valeur", nbins=10, title="Life Expectancy")

#     else:

#         x, y = 2, 2


#     fig = create_figure()

#     fig.add_trace(go.Scatter(x=[x], y=[y], marker=dict(size=15, color='green'), mode='markers'))

#     return fig

# #--------------------------------Rows------------------------------#
# row_graphs = dbc.Row(
#     [
#         row_dropdown,
#         dbc.Col(""),
#         dbc.Col(html.Div(dcc.Graph(id="graph")), width=12),
#         dbc.Col(""),
#     ],
# )


# #--------------------------------Layout------------------------------#

# layout = dbc.Container([
#     dbc.Row([
#         html.Center(html.H1("Tree Map")),
#         html.Br(),
#         html.Hr(),
#         row_graphs,

#     ])
# ])



# # On defini le layout de la page 1
# layout = dbc.Container([
#     dbc.Row([
#         html.Center(html.H1("ACCUEIL")),
#         html.Br(),
#         html.Hr(),
#    html.Div(["Input: ",
#              dcc.Input(id='my-input', value='initial value', type='text')]),
#     html.Br(),
#     html.Div(id='my-output'),
#     ])
# ])


# # =========  Callbacks  =========== #
# # Pop-up receita
# @app.callback(


#     Output(component_id='my-output', component_property='children'),
#     Input(component_id='my-input', component_property='value')
# )


# def update_output_div(input_value):
#     return 'Output: {}'.format(input_value)

# def update_output(input_value):
#     pop_2017 = pop.loc[pop['Année'] == input_value]
#     return fig1


# def open_toast(n):
#     if n == 1:
#         return no_update
#     return True

# Import libraries nécessaires
from dash import html
import dash_bootstrap_components as dbc
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from app import app

# Charger les données pour les exemples
aide = pd.read_csv("data/aide_alimentaire.csv", delimiter=",")
dispo = pd.read_csv("data/dispo_alimentaire.csv", delimiter=",")
pop = pd.read_csv("data/population.csv", delimiter=",")
inséc = pd.read_csv("data/sous_nutrition.csv", delimiter=",")
df = pd.read_csv("data/df_merge.csv", delimiter=",", low_memory=False)

#--------------------------------------- Question 1-----------------------------#

#On remplace par la date intervalle
insecurite = inséc.replace(['2012-2014', '2013-2015', '2014-2016', '2015-2017','2016-2018','2017-2019'],
                        ['2013', '2014', '2015', '2016','2017','2018'])
#Les valeurs de population sont des strings, je fais un changement vers des floats
#Les valeurs <0.1 seront considérées comme nulles dans nos calculs
insecurite['Valeur'] = insecurite['Valeur'].replace('<0.1', 0)
insecurite['Valeur'] = insecurite['Valeur'].astype('float64')
#supression des NaN
insecurite = insecurite.dropna()
sous_nutrition_pourcentage = insecurite["Valeur"].value_counts(normalize=True).mul(100).round(2).astype(str) + '%'




layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 2015, 'value': 2015},
            {'label': 2016, 'value': 2016},
            {'label': 2017, 'value': 2017},
            {'label': 2018, 'value': 2018}
        ],
        value=2017
    ),
    html.Div(id='output-div'),
])

@app.callback(
    Output('output-div', 'children'),
    [Input('my-dropdown', 'value')])

def update_output(selected_value):
    pop_year = pop.loc[pop['Année'] == selected_value]
    total = 0
    for value in pop_year['Valeur']:
        total += value
    pop_mondial_year = total / 1e3

    if selected_value == 2017:
        insecurite_mondial_year = 535.7
    elif selected_value == 2018:
        insecurite_mondial_year = 789
    elif selected_value == 2019:
        insecurite_mondial_year = 123
    else:
        insecurite_mondial_year = 0
    proportion_sous_nutrition = round((insecurite_mondial_year  / pop_mondial_year) * 100, 2)


    filtered_data = get_filtered_data(selected_value)
    # table = html.Table(
    #     [html.Tr([html.Th(col) for col in filtered_data.columns])] +
    #     [html.Tr([html.Td(filtered_data.iloc[i][col]) for col in filtered_data.columns]) for i in range(len(filtered_data))]
    # )

    df_kcal = filtered_data[['Zone','Disponibilité alimentaire (Kcal/personne/jour)']]
    df_q2 = df_kcal.groupby(['Zone']).sum()
    df_pop_2017= filtered_data[['Zone','population']]
    df_pop_2017 = df_pop_2017.drop_duplicates()
    Q2= df_pop_2017.merge(df_q2, how='inner', on='Zone')
    Q2['dispo_total_kcal']= Q2['Disponibilité alimentaire (Kcal/personne/jour)']*(Q2['population']* 1e3)
    nbre_total_pers_theorique = Q2['dispo_total_kcal'].sum() / 2500
    pourcentage = nbre_total_pers_theorique/ (  pop_mondial_year  * 1e6) * 100
    pourcentage = "{:.0f}%".format(pourcentage)

    df_veg = filtered_data[['Zone','Disponibilité alimentaire (Kcal/personne/jour)', 'Origine']]
    df_veg = df_veg.loc[df_veg['Origine'] == 'vegetale']
    df_vegetable = df_veg.groupby(['Zone']).sum()
    Q3= df_pop_2017.merge(df_vegetable, how='inner', on='Zone')
    Q3['dispo_total_kcal']= Q3['Disponibilité alimentaire (Kcal/personne/jour)']*(Q3['population']* 1e3)
    nbre_total_pers_theorique_veg = Q3['dispo_total_kcal'].sum() / 2500
    pourcentage_veg = nbre_total_pers_theorique_veg / ( pop_mondial_year* 1e6) * 100
    pourcentage_veg = "{:.0f}%".format(pourcentage_veg )


    return  html.Div('En {} proportion de la population en sous-nutrition est de {} , la disponibilité alimentaire des produits végétaux est {}'.format(selected_value, pourcentage, pourcentage_veg))
#  return  html.Div('La proportion de la population en sous-nutrition en {} ', html.Br(), 'est de {}% ', html.Br(),'t {}'.format(selected_value, pourcentage, pourcentage_veg))


def get_filtered_data(selected_value):
    filtered_data = df[df['Année'] == selected_value]
    return filtered_data

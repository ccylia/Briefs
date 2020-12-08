#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app import app
import dash_table
import pandas as pd

import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px
import plotly.graph_objs as go


df = pd.read_csv('/home/cecilia/Documents/brief/brief_dash_université/université_dash_l/timesData.csv')
df2 = df[:50]
fig = px.scatter(df, x='income', y='international', color='year', title='Score de transfert de connaissance par rapport aux perspectives international par année')


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'])

layout = html.Div(children=[
    html.Div(children=[
        html.H1(
            children='Classement des Universités',
            style={
                'textAlign': 'center',
                }
            )
        ]),
    html.Div( children=html.Div(
             'Exploration des données brut, 50 premières',
         style={
        'textAlign': 'center',
    })
        ),
    html.Div([
        dash_table.DataTable(
            data=df2.to_dict('records'),
            export_format='csv',
            columns=[{'id': c, 'name': c} for c in df2.columns],
            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_table={'overflowX': 'auto',
                         'width' : '1200px',
                         'height': '400px'},
            style_cell={
                'height': 'auto',
                'width': 'auto',
                'whiteSpace': 'normal',
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white'
                }
            )
        ]),
    html.Div(style={'backgroundColor': colors['background']}, children=[
        html.H1(
            children='Graphiques pour mise en évidence de corrélation',
            style={
                'textAlign': 'center',
                'color': colors['text']
                }
            )
        ]),

    html.Div(style={'backgroundColor': colors['background']}, 
             children=html.Div(
             'Nuage de point',
         style={
        'textAlign': 'center',
        'color': colors['text']
    })
        ),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
        )
    ])

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
from app import app
import pandas as pd
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
import base64

df = pd.read_csv('/home/cecilia/Documents/brief/brief_dash_université/université_dash_l/timesData.csv') 

image_filename = '/home/cecilia/Documents/brief/brief_dash_université/université_dash_l/apps/image.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

image_filename1 = '/home/cecilia/Documents/brief/brief_dash_université/université_dash_l/apps/index1.png'
encoded_image1 = base64.b64encode(open(image_filename1, 'rb').read())

image_filename2 = '/home/cecilia/Documents/brief/brief_dash_université/université_dash_l/apps/index2.png'
encoded_image2 = base64.b64encode(open(image_filename2, 'rb').read())

image_filename3 = '/home/cecilia/Documents/brief/brief_dash_université/université_dash_l/apps/index3.png'
encoded_image3 = base64.b64encode(open(image_filename3, 'rb').read())


from plotly.subplots import make_subplots

years = df.year.unique()
fig = make_subplots(rows=3, cols=2, start_cell="bottom-left",shared_xaxes=True, shared_yaxes=True)
xy = [(1,1), (1,2), (2,1), (2,2), (3,1), (3,2) ]
for i in range(len(years)):
    dfy=df.loc[df.year == years[i]]
    fig.add_trace(go.Scatter(x=dfy.income, y=dfy.international, mode='markers', name=str(years[i]))
              ,row=xy[i][0], col=xy[i][1])

fig.update_xaxes(title_text="income", row=1,col=2)   
fig.update_xaxes(title_text="income", row=1,col=1) 
fig.update_yaxes(title_text="international", row=2, col=1)
fig.update_layout(height=800, width=1200, title_text="Income in relation to international per year")



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
            children='Dash p2',
            style={
                'textAlign': 'center',
                }
            )
        ]),

    html.Div(children=[
        html.Img(
            src='data:image/png;base64,{}'.format(encoded_image.decode())
            )
        ]),

    html.Div(children=[
        html.H3(
            children='Cercles de corrélations',
            style={
                'textAlign': 'center',
                }
            )
        ]),   

    html.Div(children=[
        html.Img(
            src='data:image/png;base64,{}'.format(encoded_image1.decode()),
            style={
                #'height': '50%',
                #'width': '50%',
                #'textAlign': 'center'
                
                }   
            )
        ]),

    html.Div(children=[
        html.Img(
            src='data:image/png;base64,{}'.format(encoded_image2.decode())
            )
        ]),   
    html.Div(children=[
        html.Img(
            src='data:image/png;base64,{}'.format(encoded_image3.decode())
            )
        ]),   

    dcc.Graph(
        id='example-graph-3',
        figure=fig
        )

    ])















# -*- coding: utf-8 -*-

from .Dash_fun import apply_layout_with_auth, load_object, save_object

from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])


url_base = '/dash/app2/'


def Add_Dash(server):
    app = Dash(server=server, url_base_pathname=url_base, external_stylesheets=external_stylesheets)
    apply_layout_with_auth(app, layout)
    
    @app.callback(
        Output('graph-with-slider', 'figure'),
        [Input('year-slider', 'value')])
    def update_figure(selected_year):
        filtered_df = df[df.year == selected_year]
    
        fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp", 
                        size="pop", color="continent", hover_name="country", 
                        log_x=True, size_max=55)
    
        fig.update_layout(transition_duration=500)
    
        return fig
        
    return app.server
    
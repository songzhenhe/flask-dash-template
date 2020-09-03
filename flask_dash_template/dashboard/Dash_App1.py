# -*- coding: utf-8 -*-

from .Dash_fun import apply_layout_with_auth, load_object, save_object

from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div(["Input: ",
              dcc.Input(id='my-input', value='initial value', type='text')]),
    html.Br(),
    html.Div(id='my-output'),

])

url_base = '/dash/app1/'

def Add_Dash(server):
    app = Dash(server=server, url_base_pathname=url_base, external_stylesheets=external_stylesheets)
    apply_layout_with_auth(app, layout)

    @app.callback(
        Output(component_id='my-output', component_property='children'),
        [Input(component_id='my-input', component_property='value')]
    )
    def update_output_div(input_value):
        return 'Output: {}'.format(input_value)
    
    return app.server
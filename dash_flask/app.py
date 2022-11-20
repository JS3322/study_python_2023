from flask import Flask
from dash import Dash

# //https://kibua20.tistory.com/216

app = Flask(__name__)
dash_app1 = Dash(__name__, server = app, url_base_pathname='/dashapp1/')


@app.route('/')
def hello_world():  # put application's code here
    print('hello world')
    return 'index'


if __name__ == '__main__':
    app.run()

import dash_core_components as dcc
import dash_html_components as html

dash_app1.layout = html.Div([
    html.H1('Hello Dash'),
    html.Div([
        html.P('Dash converts Python classes into HTML'),
        html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
    ])
])

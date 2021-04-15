import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ClientsideFunction

from app import app
import __init__
import pages.layout
import pages.about

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/page_home':
        return pages.layout.main_layout
    elif pathname == '/page_about':
        return pages.about.main_about
    else:
        return pages.layout.main_layout


if __name__ == '__main__':
    app.run_server(debug=True)

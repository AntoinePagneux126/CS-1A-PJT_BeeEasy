from __init__ import *
from pages.nav import *
from dashboard.controle_layout import *
import datetime

from app import app


main_about = html.Div(
    [
        navbar,  # add the navbar from nav.py

        html.Br(),  # Vertical space
        html.Br(),

        dbc.Card([
            
                    dbc.Toast(
                            [html.P("Projet de ruche connectée de l'école CentraleSupélec.")],
                            id="msg",
                            header="Bee Easy",
                            icon="primary",
                            dismissable=False,
                            className='container bg-alert rounded',
                    ),

                    dbc.Toast(
                            [html.A("https://github.com/AntoinePagneux126/PJT_BeeEasy.git")],
                            id="msg-git",
                            header="GitHub",
                            icon="primary",
                            dismissable=False,
                            className='container bg-alert rounded',
                    ),
                    
        ],
            body=True,
            className='container bg-secondary rounded',
        ),
        html.Div(id='page-mainabout-content'),
    ],
)
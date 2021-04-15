from __init__ import *
from pages.nav import *
from dashboard.controle_layout import *
import datetime

from app import app

# definition of the main layout
main_layout = html.Div(
    [
        navbar,  # add the navbar from nav.py

        html.Br(),  # Vertical space
        html.Br(),

        # Timer which triggers every 60 sec
        dcc.Interval(id='interval1', interval=20 * 1000, n_intervals=0),

        dbc.Card([
            dbc.FormGroup(
                [
                    dbc.Label("Apiculteurs "),
                    dcc.Dropdown(
                        options=get_dic_beekeepers_name(),
                        id="Apiculteurs",
                    ),
                ],
            ),
            dbc.FormGroup(
                [
                    dbc.Label("Ruches "),
                    dcc.Dropdown(
                        options=[],
                        id="Ruches",
                    ),
                ]
            ),
        ],
            body=True,
            className='container bg-secondary rounded',

        ),

        html.Br(),  # Vertical space

        # Row for honey production and mass of beehive
        html.Div(
            [
                html.Br(),  # Vertical space

                dbc.Row([
                    html.Img(src='data:image/png;base64,{}'.format(encoded_image_honey.decode()),
                             height=40,
                             style={"margin-right": "30px"},
                             ),

                    html.H1("Production de miel",
                            className="text-center text-white"),
                    html.Img(src='data:image/png;base64,{}'.format(encoded_image_honey.decode()),
                             height=40,
                             style={"margin-left": "30px"},
                             ),
                ],
                    justify='center'
                ),

                html.Br(),  # Vertical space

                dbc.Row([

                    dbc.Col(
                        html.Div([
                            html.Br(),  # Vertical space
                            html.H1("Masse de la ruche : ",
                                        className="text-center text-white"),
                            html.H1(
                                children='45kg',
                                id='beehive_masse',
                                className="text-center text-white"),
                            html.Br(),  # Vertical space
                        ],
                            className='container bg-primary rounded'
                        ),
                    ),

                    dbc.Col(
                        html.Div([
                            html.Br(),  # Vertical space
                            html.H1("Quantité de miel estimée : ",
                                    className="text-center text-white"),
                            html.H1(
                                children="30 kg ",
                                id='honey_quantity',
                                className="text-center text-white"),
                            html.Br(),  # Vertical space
                        ],
                            className='container bg-primary rounded'
                        ),
                    ),

                ],
                ),

                html.Br(),  # Vertical space


                html.H1("Production avant récolte",
                        className="text-center text-white"),

                html.Br(),  # Vertical space

                dbc.Progress(
                    "",
                    value=75,
                    id='honey_progress',
                    color="success",
                    style={"height": "30px"}
                ),

                html.Br(),  # Vertical space

            ],
            className='container bg-danger rounded',
        ),

        html.Br(),  # Vertical space

        # Div for temperature, pressure and humidity
        html.Div([
            html.Br(),  # Vertical space
            dbc.Row(
                [
                        dbc.Col(
                            html.Div([
                                html.Br(),  # Vertical space

                                html.H1("Température",
                                        className="text-center text-white"),

                                dbc.Row([
                                        html.Img(src='data:image/png;base64,{}'.format(encoded_image_thermometer.decode()),
                                                 height=40,
                                                 style={"margin-right": "5px"},
                                                 ),

                                        html.H1(
                                            children="0°C",
                                            id='temperature',
                                            className="text-center text-white"),

                                        ],
                                        justify='center',
                                        ),



                                html.Br(),  # Vertical space

                            ],
                                className='container bg-success rounded'
                            ),
                            # width=3,
                        ),


                    dbc.Col(html.Div([
                            html.Br(),  # Vertical space

                            html.H1("Pression",
                                    className="text-center text-white"),

                            dbc.Row([


                                html.Img(src='data:image/png;base64,{}'.format(encoded_image_pressure.decode()),
                                         height=40,
                                         style={
                                    "margin-right": "15px"},
                                ),

                                html.H1(
                                    children="993 hPa",
                                    id='pressure',
                                    className="text-center text-white"),


                            ],
                                justify='center',
                            ),



                            html.Br(),  # Vertical space
                            ],
                        className='container bg-primary rounded'
                    ),
                            # width=3,
                        ),

                    dbc.Col(html.Div([
                            html.Br(),  # Vertical space


                            html.H1("Humidité",
                                    className="text-center text-white"),

                            dbc.Row([
                                html.Img(src='data:image/png;base64,{}'.format(encoded_image_water.decode()),
                                         height=40,
                                         style={
                                    "margin-right": "5px"},
                                ),

                                html.H1(
                                    children="50 %",
                                    id='humidity',
                                    className="text-center text-white"),


                            ],
                                justify='center',
                            ),


                            html.Br(),  # Vertical space
                            ],
                        className='container bg-warning rounded'
                    ),
                            # width=3,
                        ),

                ],
            ),
            html.Br(),  # Vertical space
        ],
            className='container bg-secondary rounded',
        ),


        html.Br(),  # Vertical space

        dbc.Card([
            dbc.FormGroup(
                    [
                        dbc.Label("Afficher "),
                        dcc.Dropdown(
                            options=[],
                            id="Mesures",
                            className="m-1",
                        ),
                    ],
            ),
            dbc.FormGroup(
                [
                    dbc.Label("Selectionner l'intervalle de temps "),
                    html.Br(),  # Vertical space
                    dcc.DatePickerRange(
                        id='my-date-picker-range',
                        className="m-1",
                    ),
                ],
            ),
            dbc.FormGroup(
                [
                    dbc.Label(children = "title", id= 'graph-title'),
                    dcc.Graph(
                        id='graph',
                        className="center rounded",
                    ),
                ],
            ),

        ],
            body=True,
            className='container bg-primary rounded',

        ),

        html.Br(),  # Vertical space
        html.Br(),  # Vertical space

        html.Div(id='page-mainlayout-content'),

    ],
)


@app.callback(
    Output("Ruches", "options"),
    Input("Apiculteurs", "value")
)
def update_dropdown_hives(beekeeper_name: str):
    """ Update the dropdown menu related to the hives of a beekeeper.

    Parameters
    ----------
    beekeeper_name : str
        Name of the beekeeper.

    Returns
    -------
    List of dict :
        {"label" : "", "value" : ""}
        that contains the name of the hive as label and value.

    """
    if beekeeper_name != None:
        return get_dic_hive_of_beekeeper(beekeeper_name)
    else:
        return []


@app.callback(
    Output("Mesures", "options"),
    Input("Ruches", "value")
)
def update_dropdown_measures(hive_name: str):
    """ Update the dropdown menu related to the measures that are possible to have from a hive.

    Parameters
    ----------
    hive_name : str
        The name of the hive.

    Returns
    -------
    List of dict :
        {"label" : "", "value" : ""}
        that contains the name of the hive as label and value.

    """
    if hive_name != None:
        return get_dic_measures(hive_name)
    else:
        return []


@app.callback(
    [
        Output("my-date-picker-range", "start_date"),
        Output("my-date-picker-range", "end_date"),
    ],
    [
        Input("Ruches", "value"),
        Input("Mesures", "value")
    ]

)
def update_date_range(hive_name: str, measure: str):
    """ Update the chart.

    Parameters
    ----------
    hive_name : str
        The name of the hive.
    measure : str
        The measure related to the hive that the user want to show.

    Returns
    -------
    A plotly figure.

    """
    if hive_name != None and measure != None:
        return get_data_range(hive_name, measure)
    else:
        return None, None


@app.callback(
    [
        Output("graph", "figure"),
        Output("graph-title", "children"),
    ],
    [
        Input("Ruches", "value"),
        Input("Mesures", "value"),
        Input("my-date-picker-range", "start_date"),
        Input("my-date-picker-range", "end_date")
    ]

)
def update_chart(hive_name: str, measure: str, start_date, end_date):
    """ Update the chart.

    Parameters
    ----------
    hive_name : str
        The name of the hive.
    measure : str
        The measure related to the hive that the user want to show.

    Returns
    -------
    A plotly figure.

    """
    title = ""
    if hive_name == None and measure == None:
        return px.line(x=[0], y=[0]), title
    else:
        if measure != None and hive_name != None:
            title = measure + " de la ruche " + hive_name
        return get_fig_for_graph(hive_name, measure, start_date, end_date), title


@app.callback(
    [
        Output('beehive_masse', 'children'),
        Output('honey_quantity', 'children'),
        Output('honey_progress', 'value'),
        Output('temperature', 'children'),
        Output('pressure', 'children'),
        Output('humidity', 'children'),
    ],
    [
        Input('interval1', 'n_intervals'),
        Input("Ruches", "value")
    ]


)
def update_information_labels(n, hive_name):
    """ Update all the label at each top of the trigger.

    Parameters
    ----------
    n : int
        The number of top count.
    hive_name : str
        The name of the hive.

    Returns
    -------
    Lists of the values espected.
    """

    print("Update n°" + str(n))
    beehive_masse = ["0" + " kg"]
    honey_quantity = ["0" + " kg"]
    honey_progress = 0
    temperature = ["0" + " °C"]
    pressure = ["0" + " hPa"]
    humidity = ["0" + " %"]

    if hive_name != None:
        beehive_masse = [str(get_last_data(hive_name, "Masse")) + " kg"]
        honey_quantity = [str(get_last_data(hive_name, "Miel")) + " kg"]
        honey_progress = n % 100
        temperature = [str(get_last_data(hive_name, "Temperature")) + " °C"]
        pressure = [str(get_last_data(hive_name, "Pression")) + " hPa"]
        humidity = [str(get_last_data(hive_name, "Humidite")) + " %"]

    return beehive_masse, honey_quantity, honey_progress, temperature, pressure, humidity


if __name__ == '__main__':
    app.run_server(debug=True)

from __init__ import *
from nav import *



# definition of layout
app.layout = html.Div(
    [
        navbar, # add the navbar from nav.py

        html.Br(),  # Vertical space
        html.Br(),


        # Row for honey production and mass of beehive
        html.Div(
            [
                html.Br(),  # Vertical space
                
                dbc.Row([
                    html.Img(src='data:image/png;base64,{}'.format(encoded_image_honey.decode()),
                                height = 40,
                                style={"margin-right": "30px"},
                            ),

                    html.H1("Production de miel",
                        className="text-center text-white"),
                    html.Img(src='data:image/png;base64,{}'.format(encoded_image_honey.decode()),
                                height = 40,
                                style={"margin-left": "30px"},
                            ),
                ],
                    justify = 'center'
                ),
                
                html.Br(),  # Vertical space

                dbc.Row([

                    dbc.Col(
                        html.Div([
                                html.Br(),  # Vertical space
                                html.H1("Masse de la ruche : ",
                                        className="text-center text-white"),
                                html.H1("45 kg",
                                        id = 'beehive_masse',
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
                            html.H1("30 kg ",
                                    id = 'honey_quantity',
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
                        "75%",
                        value=75,
                        id = 'honey_progress',
                        color="primary",
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
                                            height = 40,
                                            style={"margin-right": "5px"},
                                        ),

                                        html.H1("0°C",
                                                id = 'temperature',
                                                className="text-center text-white"),

                                    ],
                                        justify = 'center',
                                    ),

                                    
                                    
                                    html.Br(),  # Vertical space

                                    ],
                                    className='container bg-success rounded'
                                ),
                                #width=3,
                            ),


                        dbc.Col(html.Div([
                                    html.Br(),  # Vertical space

                                    html.H1("Pression",
                                            className="text-center text-white"),

                                    dbc.Row([


                                        html.Img(src='data:image/png;base64,{}'.format(encoded_image_pressure.decode()),
                                            height = 40,
                                            style={"margin-right": "15px"},
                                        ),

                                        html.H1("993 hPa",
                                            id = 'pressure',
                                            className="text-center text-white"),

                                        
                                    ],
                                        justify = 'center',
                                    ),

                                   
                                    
                                    html.Br(),  # Vertical space
                                ],
                                    className='container bg-primary rounded'
                                ),
                                #width=3,
                            ),

                        dbc.Col(html.Div([
                                    html.Br(),  # Vertical space

                                    
                                    html.H1("Humidité",
                                        className="text-center text-white"),

                                    dbc.Row([
                                         html.Img(src='data:image/png;base64,{}'.format(encoded_image_water.decode()),
                                            height = 40,
                                            style={"margin-right": "5px"},
                                        ),

                                        html.H1("50 %",
                                            id = 'humidity',
                                            className="text-center text-white"),

                                        
                                    ],
                                        justify = 'center',
                                    ),

                                    
                                    html.Br(),  # Vertical space
                                ],
                                    className='container bg-warning rounded'
                                ),
                                #width=3,
                            ),

                        ],
                        ),
                        html.Br(),  # Vertical space
                    ],
                    className='container bg-secondary rounded',
                ),
                

        html.Br(),  # Vertical space

        # Row for graph
        dbc.Row(
            [
                html.Div([
                    html.Br(),  # Vertical space
                    dcc.Graph(
                        id='graph',
                        className="center rounded",
                    ),  # Graph to show data
                    html.Br(),  # Vertical space
                ],
                className="container bg-primary rounded",
                
                ),

                

            ],
            
            ),

        html.Br(),  # Vertical space    
        html.Br(),  # Vertical space  
        
    ]
)






if __name__ == '__main__':
    app.run_server(debug=True)
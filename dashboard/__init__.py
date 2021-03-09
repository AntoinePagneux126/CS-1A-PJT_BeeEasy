import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ClientsideFunction
import plotly.express as px
import base64

# stylesheet and title
BS = "https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/lumen/bootstrap.min.css"
app = dash.Dash(
    external_stylesheets=[BS],
    title =  "Bee Easy"
)

#images
ico_directory = 'ico/'

image_hexa = ico_directory + 'hexa.png'
encoded_image_hexa = base64.b64encode(open(image_hexa, 'rb').read())

image_honey = ico_directory + 'honey.png'
encoded_image_honey = base64.b64encode(open(image_honey, 'rb').read())

image_thermometer = ico_directory + 'thermometer.png'
encoded_image_thermometer = base64.b64encode(open(image_thermometer, 'rb').read())

image_water = ico_directory + 'water.png'
encoded_image_water = base64.b64encode(open(image_water, 'rb').read())

image_pressure = ico_directory + 'pressure.png'
encoded_image_pressure = base64.b64encode(open(image_pressure, 'rb').read())


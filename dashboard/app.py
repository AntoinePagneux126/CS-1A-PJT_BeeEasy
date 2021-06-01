import dash


# stylesheet and title
BS = "https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/lumen/bootstrap.min.css"
app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[BS],
    title =  "Bee Easy"
)

server = app.server
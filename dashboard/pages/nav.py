from __init__ import *

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"


collapse = dbc.Row(
    [
        dbc.Col(
            dbc.Button("Home", color="primary", href = "/page_home",className="ml-2", id = "home"),
            width="auto",
        ),
        dbc.Col(
            dbc.Button("A propos", color="primary", href = "/page_about", className="ml-2", id = "about"),
            width="auto",
        ),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",

)

navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src='data:image/png;base64,{}'.format(encoded_image_hexa.decode()),
                                height = 60,
                            )),
                    dbc.Col(dbc.NavbarBrand(html.H2("Bee Easy"), className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="/page_home", #mettre la ref de beeeasy
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(collapse, id="navbar-collapse", navbar=True),
    ],
    color="primary",
    dark=True,
)


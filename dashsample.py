import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("My First Dash App"),
    html.H2("This is a simple header example"),
    html.H3("A smaller header"),
])

if __name__ == '__main__':
    app.run_server(debug=True)
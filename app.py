import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

app = Dash()

df = pd.read_csv(r".\coffee_shop_revenue.csv")

fig = px.bar(df, x="Number_of_Employees", y="Number_of_Customers_Per_Day", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
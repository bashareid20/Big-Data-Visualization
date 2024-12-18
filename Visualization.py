import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Initialize Dash app
app = Dash(__name__)

# Sample dataset: COVID-19 Data (replace with large dataset in practice)
url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.csv'
data = pd.read_csv(url)

# Data preprocessing
data = data[['location', 'total_cases', 'total_deaths', 'population']]
data = data.dropna()
data['cases_per_million'] = (data['total_cases'] / data['population']) * 1e6

# App layout
app.layout = html.Div([
    html.H1("Big Data Visualization Dashboard", style={'textAlign': 'center'}),

    dcc.Dropdown(
        id='metric-selector',
        options=[
            {'label': 'Total Cases', 'value': 'total_cases'},
            {'label': 'Total Deaths', 'value': 'total_deaths'},
            {'label': 'Cases per Million', 'value': 'cases_per_million'}
        ],
        value='total_cases',
        style={'width': '50%', 'margin': 'auto'}
    ),

    dcc.Graph(id='bar-chart')
])

# Callback to update chart
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('metric-selector', 'value')]
)
def update_chart(selected_metric):
    fig = px.bar(
        data.sort_values(by=selected_metric, ascending=False).head(20),
        x='location',
        y=selected_metric,
        title=f"Top 20 Countries by {selected_metric.replace('_', ' ').title()}",
        labels={'location': 'Country', selected_metric: selected_metric.replace('_', ' ').title()},
        template='plotly'
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

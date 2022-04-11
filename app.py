import pandas as pd
from dash import Dash, dcc, html, Input, Output
import json
import random
from src.hex_fig import get_hex_fig, hex_point_groups
from src.location_blurb import click_to_lat_lon

# temporarily trimming dataset for testing
# generate fake fire data per location
locations = json.load(open('data/locations.json'))
mock_df = pd.DataFrame(
    [
        location + [random.random(), random.randint(2018, 2021)]
        for location in locations[::15]
    ],
    columns=['lat', 'lon', 'fire_score', 'year']
)


app = Dash(__name__)
server = app.server
app.layout = html.Div([
    html.H3(
        id='weather-blurb'
    ),

    dcc.Graph(
        figure=get_hex_fig(mock_df),
        id='fire-graph',
        className='bordered'
    ),

    dcc.Markdown(
        '''
        # Click Hex To See Underlying Data
        ''',
        id='click-receiver',
        style={'text-align': 'left'}
    )
], style={'text-align': 'center'})


# click callback example
@app.callback(
    Output('click-receiver', 'children'),
    [Input('fire-graph', 'clickData')]
)
def display_location(clickData):
    point_num = clickData['points'][0]['pointNumber']
    hex_data = hex_point_groups[point_num]
    lat, lon = click_to_lat_lon(clickData)
    data_str = ', '.join([f'{d:.3f}' for d in hex_data])
    blurb = (
        f'# Data For Hex At \n'
        f'### Lon: {lon:.3f}\N{DEGREE SIGN} \n'
        f'### Lat: {lat:.3f}\N{DEGREE SIGN} \n'
        f'{data_str}'
    )
    return blurb


if __name__ == '__main__':
    app.run_server(debug=True)

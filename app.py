from dash import Dash, dcc, html, Input, Output
from src.hex_fig import hex_fig, agg_and_record, hex_point_groups
from src.location_blurb import click_to_lat_lon
from src.data import get_wildfire_data

df = get_wildfire_data()

app = Dash(__name__)
server = app.server
app.layout = html.Div([
    html.H3(
        id='weather-blurb'
    ),

    dcc.Graph(
        figure=hex_fig(df, "fire_prob", agg_and_record),
        id='fire-graph',
        className='bordered'
    ),

    dcc.Markdown(
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
    if not clickData:
        return '# Click Hex to See Underlying Data'
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

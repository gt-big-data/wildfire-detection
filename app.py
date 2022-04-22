from dash import Dash, dcc, html, Input, Output, State
from src.hex_fig import hex_fig, hex_point_groups
from src.location_blurb import click_to_lat_lon
from src.data import get_wildfire_data, get_mock_data
from numpy import mean

real_fig = hex_fig(get_wildfire_data(), "fire_prob", mean, 20)
mock_fig = hex_fig(get_mock_data(), "fire_prob", mean, 60)

app = Dash(__name__)
server = app.server
app.layout = html.Div([
    dcc.Markdown(
        (
            '# Wildfire Detection\n'
            'Each hexagon\'s color tells you how likely a wildfire '
            'is to occur within it. This probability score is actually '
            'an average over the probabilities computed at many points '
            'within the hex.'
        )
    ),

    html.H3(
        id='weather-blurb'
    ),

    # html.Button(
    #     'Switch Figure',
    #     id='switch-button',
    #     n_clicks=0
    # ),

    dcc.Graph(
        figure=real_fig,
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
        return '# Click Hex to See Underlying Point Estimates'
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


# @app.callback(
#     Output('fire-graph', 'figure'),
#     Input('switch-button', 'n_clicks')
# )
# def switch_fig(n_clicks):
#     if n_clicks % 2 == 0:
#         return real_fig
#     else:
#         return mock_fig


if __name__ == '__main__':
    app.run_server(debug=True)

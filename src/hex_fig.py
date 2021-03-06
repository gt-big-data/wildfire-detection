import plotly.figure_factory as ff

hex_point_groups = []

HEX_ST = {
    'map': 'carto-positron',
    'font-size': 14,
    'font-fam': 'Roboto Mono, monospace',
    'bg': '#FF7F50',
    'w': None,
    'h': None,
    'opac': 0.2
}


def hex_fig(df, data_col_name, agg_func, density):
    fig = ff.create_hexbin_mapbox(
        data_frame=df,
        lat="lat",
        lon="lon",
        mapbox_style=HEX_ST['map'],
        nx_hexagon=density,
        opacity=HEX_ST['opac'],
        labels={'color': data_col_name},
        color=data_col_name,
        agg_func=get_agg_and_record_func(agg_func),
        min_count=1,
        width=HEX_ST['w'],
        height=HEX_ST['h']
    )

    fig.update_layout(
        clickmode='event+select',
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        plot_bgcolor=HEX_ST['bg'],
        paper_bgcolor=HEX_ST['bg'],
        font_size=HEX_ST['font-size'],
        font_family=HEX_ST['font-fam']
    )

    # hex_fig.layout.sliders[0].pad = {"r": 0, "t": 10, "l": 20, "b": 10}
    # hex_fig.layout.updatemenus[0].pad = {"r": 0, "t": 30, "l": 10, "b": 0}
    # hex_fig.layout.updatemenus[0].x = 0.106
    # print(hex_fig.layout)

    return fig


"""
Plotly is weird.

Each hex has a "pointNumber" in its clickData (see app.py)
This corresponds to the order in which the underlying data is aggregated
"""


def get_agg_and_record_func(agg_func):
    def agg_and_record(num_list):
        hex_point_groups.append(num_list)
        return agg_func(num_list)
    return agg_and_record

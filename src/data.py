import pandas as pd
import json
import random


def get_mock_data():
    locations = json.load(open('data/locations.json'))
    df = pd.DataFrame(
        [
            location + [random.random(), random.randint(2018, 2021)]
            for location in locations[::15]
        ],
        columns=['lat', 'lon', 'fire_prob', 'year']
    )
    return df


def get_wildfire_data():
    df = pd.read_csv(
        'analysis/final_demo_analysis/wildfire_predictions.csv',
        index_col=0
    )
    df.columns = ['lat', 'lon', 'fire_prob']
    return df

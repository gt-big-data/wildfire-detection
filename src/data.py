import pandas as pd
import numpy as np

DATA_PATH = 'deploy/wildfire_predictions_v2.csv'


def get_mock_data():
    df = pd.read_csv('deploy/grid.csv', index_col=0)
    df['fire_prob'] = np.sin(df['lat']) + np.sin(df['lon'])
    return df


def get_wildfire_data():
    df = pd.read_csv(
        DATA_PATH,
        index_col=0
    )
    df.columns = ['lat', 'lon', 'fire_prob']
    return df

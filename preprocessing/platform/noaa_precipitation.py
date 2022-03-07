"""
    Converts NOAA precipitation data from text table to csv. See:
    https://www.cnrfc.noaa.gov/data/text/precip_google/PNM_Mar_2022.txt
"""
import pandas as pd
import requests


TABLE_START = 4
ROW_START = 55
BASE_URL = '''https://www.cnrfc.noaa.gov/data/text/precip_google/
              {format}_{month}_{year}.txt'''
URL_PARAMS = {
    'FORMAT': 'PNM',  # monthly precipitation
    'START_YEAR': 2012,  # data goes back to 1997, but we don't need that much
    'END_YEAR': 2022,
    'MONTH_NAMES': [
        'Jan', 'Feb', 'Mar', 'Apr',
        'May', 'Jun', 'Jul', 'Aug',
        'Sep', 'Oct', 'Nov', 'Dec'
    ]
}


def generate_urls():
    return []


def get_precipitation_txt_from_url(url):
    return ''


def precipitation_txt_to_df(txt):
    lines = txt.splitlines()[TABLE_START:]
    data = [line[ROW_START:].split() for line in lines]

    df = pd.DataFrame(data)
    df.columns = df.iloc[0]
    df = df[1:]

    return df

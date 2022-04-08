"""
    Converts NOAA precipitation data from text table to csv. See:
    https://www.cnrfc.noaa.gov/data/text/precip_google/PNM_Mar_2022.txt
"""
import logging
import requests
import pandas as pd
TABLE_START = 4
ROW_START = 55
START_YEAR = 2010
END_YEAR = 2022
MONTH_NAMES = [
    "Jan", "Feb", "Mar", "Apr",
    "May", "Jun", "Jul", "Aug",
    "Sep", "Oct", "Nov", "Dec"
]
BASE_URL = "https://www.cnrfc.noaa.gov/data/text/precip_google/PNM"


def generate_urls(month, year):
    return f'{BASE_URL}_{month}_{year}.txt'


def get_precipitation_txt_from_url(url):
    response = requests.get(url)
    content = None
    if response.status_code == 200:
        content = response.text
    else:
        logging.error(f'''
            Request failed with code {response.status_code} 
            for url {url}''')
    return content


def precipitation_txt_to_df(content, df, month, year):
    if not content:  # empty content
        return df

    lines = content.splitlines()[TABLE_START:]
    data = [line[ROW_START:].split() for line in lines]

    df2 = pd.DataFrame(data)
    df2.columns = df2.iloc[0]
    df2 = df2[1:]
    df2['Month'] = month
    df2['Year'] = year
    df = pd.concat([df, df2], ignore_index=True)

    return df


def generate_csv(df, start_year, end_year):
    df = pd.DataFrame()
    for year in range(start_year, end_year + 1):
        for month in MONTH_NAMES:
            url = generate_urls(month, year)
            content = get_precipitation_txt_from_url(url)
            df = precipitation_txt_to_df(content, df, month, year)
            print(f'Finished processing data for {month}, {year}')

    df.columns = [
        'state',
        'lat',
        'lon',
        'elevation_ft',
        'normal_precip_relative_pcnt',
        'precip_in',
        'normal_precip_in',
        'month',
        'year'
    ]
    df = df[df['state'] == 'CA']
    df = df[['lat', 'lon', 'elevation_ft', 'precip_in', 'month', 'year']]
    df.to_csv("data/noaa_precip.csv")


def test_get_noaa_data():
    df = pd.DataFrame()
    test_url = "https://www.cnrfc.noaa.gov/data/text/precip_google/PNM_Mar_2022.txt"
    content = get_precipitation_txt_from_url(test_url)
    df = precipitation_txt_to_df(content, df, 'Mar', 2022)
    df.columns = [
        'state',
        'lat',
        'lon',
        'elevation_ft',
        'normal_precip_relative_pcnt',
        'precip_in',
        'normal_precip_in',
        'month',
        'year'
    ]

    df = df[df['state'] == 'CA']
    df = df[['lat', 'lon', 'elevation_ft', 'precip_in', 'month', 'year']]
    # df.to_csv("data/test_noaa_precip.csv")


df = pd.DataFrame()
generate_csv(df, START_YEAR, END_YEAR)
# test_get_noaa_data()

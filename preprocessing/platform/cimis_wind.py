from ftplib import FTP
from shutil import unpack_archive
import glob
import pandas as pd
import os

CIMIS_WIND_FTP = 'ftp.cimis.water.ca.gov'
CIMIS_FILE_PREFIX = 'dailyStns{year}'

START_YEAR = 2010
END_YEAR = 2020

# connects to ftp server
ftp = FTP(CIMIS_WIND_FTP)
ftp.login()
ftp.cwd('pub2')


# writes file from ftp to local
def get_data_from_ftp(year):
    fname = f'dailyStns{year}'
    zip = f'data/staging/cimis/{fname}.zip'
    remote = f'RETR annual/{fname}.zip'  # forward slash needed
    dest = f'data/staging/cimis/{fname}'

    with open(zip, 'wb') as fp:
        ftp.retrbinary(remote, fp.write)

    unpack_archive(zip, dest)


def get_stations_from_ftp():
    with open('data/staging/cimis/stations.xlsx', 'wb') as fp:
        ftp.retrbinary('RETR CIMIS Stations List (January20).xlsx', fp.write)


def process_data(year, agg_df):
    wind_idx = 16 if year < 2014 else 25
    csv_paths = glob.glob(f'data/staging/cimis/dailyStns{year}/*.csv')

    def get_wind_mean(path):
        if os.stat(path).st_size == 0:
            return None
        df = pd.read_csv(path, header=None)
        wind_col = df[df.columns[wind_idx]]
        wind_col = pd.to_numeric(wind_col, errors='coerce').dropna()
        return wind_col.mean()

    rows = [
        [path[-7:-4], get_wind_mean(path), year]
        for path in
        csv_paths
    ]

    df = pd.DataFrame(rows)
    df.columns = ['station', 'wind_mph', 'year']

    return pd.concat([agg_df, df], ignore_index=True)


# agg_df = pd.read_csv('data/cimis_wind.csv')

# 
# st_df = pd.read_excel('data/staging/cimis/cimis_stations.xlsx')
# st_df = st_df[['Station Number', 'Latitude', 'Longitude']]
# st_df = st_df[st_df['Station Number'].notna()]
# st_df = st_df.astype({'Station Number': 'int64'})


# for year in range(START_YEAR, END_YEAR + 1):
#     # get_data_from_ftp(year)
#     agg_df = process_data(year, agg_df)

# agg_df = agg_df.merge(st_df[['Station Number', 'Latitude', 'Longitude']])

# agg_df.to_csv('data/cimis_wind.csv')



# cimis_df = cimis_df.merge(st_df, left_on='station', right_on='Station Number', how='left')
# cimis_df = cimis_df[['year', 'wind_mph', 'Latitude', 'Longitude']]
# cimis_df = cimis_df.dropna()
# cimis_df.columns = ['year', 'wind', 'lat', 'lon']
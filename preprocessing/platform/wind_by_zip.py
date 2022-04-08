import pandas as pd


def get_ca_zip_latlon_csv():
    zip_df = pd.read_csv('data\\staging\\zip\\zip_latlon.csv')
    zip_df = zip_df[zip_df['zip'].between(90001, 96162)]
    zip_df.reset_index()
    zip_df.to_csv('data\\staging\\zip\\ca_zip_latlon.csv')


def generate_wind_by_zip_csv():
    df = None
    with open('data\\staging\\zip\\wind_by_zip.txt') as f:
        speed_by_zip = [
            [line.split()[1], line.split()[3]]
            for line in f.readlines()
        ]

        df = pd.DataFrame(speed_by_zip)
        df.columns = ['wind_mph', 'zip']
        df = df.astype({'zip': 'int64'})

        zip_df = pd.read_csv('data\\staging\\zip\\ca_zip_latlon.csv')

        df = df.merge(zip_df, on='zip', how='left')
        df = df[['wind_mph', 'lat', 'lon']]
        df = df.dropna()

        print(df)

        df.to_csv("data\\wind_by_zip.csv")


generate_wind_by_zip_csv()

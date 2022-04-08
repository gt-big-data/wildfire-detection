import pandas as pd

df = None
with open('data/wind_by_zip.txt') as f:
    speed_by_zip = [
        [line.split()[1], line.split()[3]]
        for line in f.readlines()
    ]

    df = pd.DataFrame(speed_by_zip)
    df.columns = ['wind_mph', 'zip']
    df.to_csv("data/wind_by_zip.csv")

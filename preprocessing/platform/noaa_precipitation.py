"""
    Converts NOAA precipitation data from text table to csv. See:
    https://www.cnrfc.noaa.gov/data/text/precip_google/PNM_Mar_2022.txt
"""
import requests
import pandas as pd
TABLE_START = 4
ROW_START = 55
START_YEAR = 2000
END_YEAR = 2022

df = pd.DataFrame()
firstPartLink = "https://www.cnrfc.noaa.gov/data/text/precip_google/PNM"
Month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def generate_urls(month, year):
    monYear = ("_" + month + "_" + str(year))
    url = (firstPartLink + monYear + ".txt")
    return url


def get_precipitation_txt_from_url(url):
    data = requests.get(linkName)   # response object = contents 
    content = data.text
    return content


def precipitation_txt_to_df(content, df, month, year):
    lines = content.splitlines()[TABLE_START:]
    data = [line[ROW_START:].split() for line in lines]

    df2 = pd.DataFrame(data)
    df2 = df2.reset_index()
    df2.columns = df2.iloc[0]
    df2 = df2[1:]
    df2['Month'] = month
    df2['Year'] = year
    df = pd.concat([df, df2], ignore_index = True)
    return df

def generate_csv(df, START_YEAR, END_YEAR):
    for year in range (START_YEAR, END_YEAR + 1):
        for month in Month:
            url = generate_urls(month, year)
            content = get_precipitation_txt_from_url(url)
            df = precipitation_txt_to_df(content, df, month, year)
    df.to_csv("data_noaa_precip.csv")

generate_csv(df, START_YEAR, END_YEAR)
        

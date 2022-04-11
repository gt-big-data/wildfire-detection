# wildfire-detection


## Run with pipenv (recommended)
Pipenv is basically pip + venv. It lets you set up an isolated environment per project. Read more [here](https://pipenv.pypa.io/en/latest/install/)

> pipenv install
> 
> pipenv run python app.py

Open http://127.0.0.1:8050/ 


## Run with pip
Navigate to the project root
> pip install -r requirements.txt
> 
> python app.py

Open http://127.0.0.1:8050/ 

## Setup

After installing, make sure you select the right python interpreter.

If you're using VSCode, install the Python extension, hit 'ctrl + shift + p' and search 'select interpreter'

Note that if the dependencies change, requirements.txt must be manually generated using
> pipenv lock -r > requirements.txt

## Tests
Tests must go into the tests folder

Test files must be of form:
> test_X.py

## Linting
Style checking is done with flake8 (one of the packages installed above). 
In VSCode, hit 'ctrl + shift + p' and search 'select linter'


# Data Catalogue

## [CIMIS Wind](https://data.ca.gov/dataset/cimis-weather-station-data1/resource/32b3ba24-7ce8-461e-9812-95c739742c86)
Data - data/cimis_wind.csv

Code - preprocessing/platform/cimis_wind.py

Code - preprocessing/cimis_wind.ipynb

- wind_mph - average wind speed 
- year - [2010, 2020] inclusive


## [Wind By Zip](http://www.usa.com/rank/california-state--average-wind-speed--zip-code-rank.htm?yr=9000&dis=&wist=&plow=&phigh=)
Based on 2010-2014 census data only

Data - data/wind_by_zip.csv

Code - preprocessing/platform/wind_by_zip.py


## [NOAA Precipitation](https://www.cnrfc.noaa.gov/data/text/precip_google/PNM_Mar_2022.txt)
Data - data/noaa_precip.csv

Code - preprocessing/platform/noaa_precipitation.py

- elevation_ft
- precip_in - observed monthly precipitation (inches)
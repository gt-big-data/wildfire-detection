# wildfire-detection

## Installing dependencies
If using pipenv (recommended)
> pipenv install

If using pip
> pip install -r requirements.txt

After installing, make sure you select the right python interpreter.

If you're using VSCode, hit 'ctrl + shift + p' and search 'select interpreter'

Note that if the dependencies change, requirements.txt must be manually generated using
> pipenv lock -r > requirements.txt

## Linting
Style checking is done with flake8 (one of the packages installed above). 
Should automatically be configured for you


# Data Dictionary

## [CIMIS Wind](https://data.ca.gov/dataset/cimis-weather-station-data1/resource/32b3ba24-7ce8-461e-9812-95c739742c86)
Data - data/cimis_wind.csv

Code - preprocessing/platform/cimis_wind.py

Code - preprocessing/cimis_wind.ipynb

- wind_mph - average wind speed 
- year - [2010, 2020] inclusive
- lat
- lon


## [Wind By Zip](http://www.usa.com/rank/california-state--average-wind-speed--zip-code-rank.htm?yr=9000&dis=&wist=&plow=&phigh=)
Based on 2010-2014 census data only

Data - data/wind_by_zip.csv

Code - preprocessing/platform/wind_by_zip.py

- wind_mph
- lat
- lon
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
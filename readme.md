### CLI application to pull data from SWAPI API and perform operations on it.

#### Project Structure
```
|--- swapi_mini
   |--- resources
       |--- __init__.py
       |--- base.py
       |--- characters.py
       |--- films.py
       |--- planets.py
       |--- species.py
       |--- starships.py
       |--- vehicles.py
   |--- utils
       |--- __init__.py
       |--- fetch_data.py
       |--- logger.py
       |--- randgen.py
       |--- timeit.py
   |--- main.py
   |--- output.txt
   |--- readme.md
   |--- requirements.txt
   |--- task_one.py
   |--- task_three.py
   |--- task_two.py
    
```

#### CLI command to run the project
example:
`python main.py task_one/task_two/task_three`

- __task_one__:
  - Prints detail of 15 random characters
- __task_two__:
  - Prints name of below resources in film 1
    - Character
    - Planet
    - Vehicle
- __task_three__:
  - resources - ["Films", "People","Planet","Species","Starships","Vehicles"]
    1. get count of each resource
    2. get "singular" resource urls of each resource
    3. pull data from random 3 "singular" resource URLs


### Setup

## Create virtualenv
```
virtualenv venv
```
### Activate virtualenv
```
source venv/bin/activate
```
### Install dependencies (using virtual environment is recommended):
```
pip install -r requirements.txt
```

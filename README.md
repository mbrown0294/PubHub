# PubHub
Web application for publication data designed to give access to a database of published works, as well as allow changes to be made to that database.
## Setup
Python3.5 or higher is required, as well as the libraries in ```requirements.txt```. Before running the app, first run ```db_creator.py``` and ```db_fill.py``` (respectively) using Python in order to initialize the database and fill it with the information provided in ```endnote.txt```.
## Usage
The provided ```endnote.txt``` file includes several published works and their accompanying information (columns are delimited by tabs; for works with multiple authors, the authors are delimited by "//" and "|"). How a given ```.txt``` or ```.csv``` file is ingested is determined by ```db_fill.py```. 

In order to run the application and allow browser access, run the following terminal code:
```
FLASK_APP=main.py flask run
```
## Required Work
The project is incomplete, and therefore requires continued adjustments to ```db_fill.py``` and ```main.py``` (it cannot yet correctly return ```results.html``` with the provided information). 
### Unsolved Issues 
* Inability to join and present the various (3) tables used to store information 

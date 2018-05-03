# PubHub
Web app deisgned to give access to a database of published works, as well as allow changes to be made to that database.
## Setup
All libraries in the ```requirements.txt``` should be  installed prior to running the application. Python v2.7 or higher is required, as well. Before running the app, first run ```db_creator.py``` and ```db_fill.py``` to initialize the database and fill it with the information provided in the ```endnote.txt```.
## Usage
The provided ```endnote.txt``` file includes several published works and their accompanying information (columns are delimited by tabs; for works with multiple authors, the authors are delimited by "//"). How a given .txt or .csv file is ingested is controlled by the code in ```db_fill.py```. 

In order to run the application and allow browser access, run the following terminal code:
```
FLASK_APP=main.py flask run
```
## Required Work
The code is incomplete, and therefore requires continued adjustments to ```db_fill.py``` (depending on publication information files and selected columns), and ```main.py``` (must be able to correctly display ```results.html``` with provided information). Unsolved issues include inability to join and present the various tables used to store infomration (one for Authors, on for Works), which are necessary in order to look up works by author as well as author by works. 

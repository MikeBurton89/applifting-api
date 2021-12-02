APPLIFTING API
A REST API JSON Python microservice that allows user to browse a catalog and automatically updates prices from offer service.

To deploy on a local machine I advise to create a virtual environment, if you don't know how it's done refer to this documentation https://docs.python.org/3/library/venv.html.
(There are other libraries but I used this one, I guess it's ok to use any of the other)

After you cd to the directory, activated the virtual environment you need to install the requirements, easy peasy do it launching this command 'pip install -r requirements.txt' from your terminal (with venv activated).

Once you have installed the requirements open a python CLI and run:

from models import db

from main import create_app

app =  create_app() 

app.app_context().push()

db.create_all()

This will initialize the sqlite database you need to play with the api.

To run the server run from your terminal: 'python (or python3 on mac and Linux) app.py runserver'

Take notice that the default mode is development mode with the debug active.
If you prefer to run in production or testing mode just change the mode in app.py and main.py from 'DevConf' to 'ProdConf' or 'TestConf'.


Framework= FLASK

Database= SQLite

Product Schema:

uuid = Integer

ID = integer, unique, Primary Key, required

Name = string, required

Description = string

Relationship = 1 product to many offers

Offer Schema:

product_ID = integer, Foreign_key--> product.id

id = integer required

price = integer

stock = integer


First time using Flask for an API, as of today 2/12/2021 I'm still trying to solve some issues especially with module flask_sqlalchemy that doesn't get recognized from import statements even if its installed both in the venv and on the computer.

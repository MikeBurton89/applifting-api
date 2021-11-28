APPLIFTING API
A REST API JSON Python microservice that allows user to browse a catalog and automatically updates prices from offer service.

Framework= FLASK
Database= SQLite

Product Schema:
ID = integer, unique, Primary Key, required
Name = string, required
Description = string
Relationship = 1 product to many offers

Offer Schema:
product_ID = integer, Foreign_key--> product.id
id = integer required
price = integer
stock = integer

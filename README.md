



# How to start the app:
```
source venv\bin\activate
flask run
```

in pycharm you need to point to the venv and have module name=flask, parameters=run

# Setting up the database for the first time:

```
flask db init
```
this will generate a migrations folder 

# Database migrations
```
flask db migrate -m "users table"
```
This creates a py file based on the recent changes.  To apply the changes you need
```
flask db upgrade
```

# Using the openbeer database for the first time

ensure you have mysql installed (brew install if needed)
mysql -uroot
mysql.server start

CREATE DATABASE openbeer;
USE openbeer;
CREATE USER 'beercellar';
GRANT ALL PRIVILEGES ON *.* TO 'beercellar'@'localhost';

the openbeer database is a mysql database
create all the tables in the catalogue by running
```
mysql> source create.sql
```
for each of the sql files in catalogue/

Update your Flask configuration to point to the openbeer.db:
SQLALCHEMY_DATABASE_URI=sqlite:///openbeer.db

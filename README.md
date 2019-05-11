



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



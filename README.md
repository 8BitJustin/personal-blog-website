# Personal Blog (JODBlog)

Simple website that displays a home page for blog posts, login page for admin, and a create/edit/delete page.

The main page is accessible to anyone that is able to view normally. The
 login button will lead you to the posts page, where only the user that logs
  in can create/edit/delete posts.

## Getting Started

These instructions will advise how to create a profile for login purposes, create a database for post storage, and how to launch locally
 (instructions on how to deploy to Heroku will not be covered).

### Prerequisites

For this to work, you will want to install Flask, sqlalchemy, and flask_login.

### Installing

First, download the project folder from [here](https://github.com/8BitJustin/personal-blog).

Once this is placed in your desired folder, within your terminal/cmd
/powershell, use pip install for the needed items:

```
pip install Flask
pip install sqlalchemy
pip install flask_login
```

## Creating Databases

This will instruct how to make each database.

### User database

Before you can create a user to be able to login, you need to create a
 database for that user.
 
Within the terminal/cmd/powershell (while in the directory of the project
), go into Python. Once within Python, import both db and User:

```
from app import db, User
```

Then created the table:

```
db.create_all()
```

If there are no errors, you are good.

Now to create the user:

```
db.session.add(User(email = "desired email", password = "desired password"))
```

After creating, commit changes:

```
db.session.commit()
```

This should put the created profile in place. To test, within Python, type
 the following:
 
```
User.query.all()
```

If a 'User 1' displays, you are all set.

### Blog database

You can't have a blog site without a place to put the blog entries, right?

To create the database, just like above, enter Python, and type the following:

```
from app import db
```

And with that imported, create the database/table:

```
db.create_all()
```

Now both items should be in place. :)

## Deployment

To run this on the your local system, have a terminal/cmd/powershell window
 opened and within the directory of the project, simply input the following:
 
```
python app.py
```

The terminal should show some information, including a localhost link
. Within your browser, simply go to **localhost:5000**, which will display
 the website.

## Built With

* [Python](https://www.python.org/) - Main language used
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [SQLAlchemy](https://www.sqlalchemy.org/) - For databases
* [Flask-Login](https://flask-login.readthedocs.io/en/latest/) - User session management

## Authors

* **Justin Olson** - *Initial work* - [Github](https://github.com/8BitJustin
) / [Portfolio](https://jolsondigital.netlify.app/)

## Acknowledgments

* Udemy - The Python Mega Course
* FreeCodeCamp - Learn Flask for Python


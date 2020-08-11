# Personal Blog (JODBlog)

Simple website that displays a home page for blog posts, login page for
 admin, and a create/edit/delete page.

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
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc


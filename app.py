from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



all_posts = [
    {
        'title': 'Post 1',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
                   ' Donec leo lacus, pretium at turpis eget, lacinia'
                   ' porttitor tellus. Pellentesque ipsum mauris, pretium quis'
                   ' posuere sit amet, gravida eget augue. Orci varius natoque'
                   ' penatibus et magnis dis parturient montes, nascetur'
                   ' ridiculus mus.',
        'created': 'Jan 1, 2020 @ 8:00am'
    },
    {
        'title': 'Post 2',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
                   ' Donec leo lacus, pretium at turpis eget, lacinia'
                   ' porttitor tellus. Pellentesque ipsum mauris, pretium quis'
                   ' posuere sit amet, gravida eget augue. Orci varius natoque'
                   ' penatibus et magnis dis parturient montes, nascetur'
                   ' ridiculus mus.',
        'created': 'Jan 2, 2020 @ 8:00am'
    },
    {
        'title': 'Post 3',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
                   ' Donec leo lacus, pretium at turpis eget, lacinia'
                   ' porttitor tellus. Pellentesque ipsum mauris, pretium quis'
                   ' posuere sit amet, gravida eget augue. Orci varius natoque'
                   ' penatibus et magnis dis parturient montes, nascetur'
                   ' ridiculus mus.',
        'created': 'Jan 3, 2020 @ 8:00am'
    }
]


@app.route('/')
def index():
    return render_template('index.html', posts=all_posts)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)


@app.route('/edit')
def edit():
    return render_template('edit.html')


if __name__ == "__main__":
    app.run(debug=True)

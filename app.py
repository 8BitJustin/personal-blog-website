from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return 'Blog post ' + str(self.id)


# all_posts = [
#     {
#         'title': 'Post 1',
#         'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
#                    ' Donec leo lacus, pretium at turpis eget, lacinia'
#                    ' porttitor tellus. Pellentesque ipsum mauris, pretium quis'
#                    ' posuere sit amet, gravida eget augue. Orci varius natoque'
#                    ' penatibus et magnis dis parturient montes, nascetur'
#                    ' ridiculus mus.',
#         'created': 'Jan 1, 2020 @ 8:00am'
#     },
#     {
#         'title': 'Post 2',
#         'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
#                    ' Donec leo lacus, pretium at turpis eget, lacinia'
#                    ' porttitor tellus. Pellentesque ipsum mauris, pretium quis'
#                    ' posuere sit amet, gravida eget augue. Orci varius natoque'
#                    ' penatibus et magnis dis parturient montes, nascetur'
#                    ' ridiculus mus.',
#         'created': 'Jan 2, 2020 @ 8:00am'
#     },
#     {
#         'title': 'Post 3',
#         'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
#                    ' Donec leo lacus, pretium at turpis eget, lacinia'
#                    ' porttitor tellus. Pellentesque ipsum mauris, pretium quis'
#                    ' posuere sit amet, gravida eget augue. Orci varius natoque'
#                    ' penatibus et magnis dis parturient montes, nascetur'
#                    ' ridiculus mus.',
#         'created': 'Jan 3, 2020 @ 8:00am'
#     }
# ]


@app.route('/')
def index():
    all_posts = BlogPost.query.order_by(BlogPost.created).all()
    return render_template('index.html', posts=all_posts)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        new_post = BlogPost(title=post_title, content=post_content)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.created).all()
        return render_template('posts.html', posts=all_posts)


@app.route('/edit')
def edit():
    return render_template('edit.html')


if __name__ == "__main__":
    app.run(debug=True)

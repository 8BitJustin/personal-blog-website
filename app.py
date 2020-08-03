from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/posts')
def posts():
    return render_template('posts.html')


@app.route('/edit')
def edit():
    return render_template('edit.html')


if __name__ == "__main__":
    app.run(debug=True)

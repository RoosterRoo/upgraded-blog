from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/74ec013056be49b74cf7")
all_posts = response.json()


@app.route('/')
def home():
    return render_template('index.html', posts=all_posts)


@app.route('/post/<int:num>')
def get_blog(num):
    return render_template('post.html', post=all_posts[num - 1])


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)

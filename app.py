from flask import Flask, render_template, jsonify

app = Flask(__name__)

BLOGS = [
    {
        'id' : 1,
        'title' : 'Hello, world',
        'content' : 'Lorem ipsum dolor sit amet',
        'author' : 'John Doe'
    },
    {
        'id' : 2,
        'title' : 'Hello, country',
        'content' : 'Lorem ipsum dolor sit amet',
        'author' : 'John Doe'
    },
    {
        'id' : 3,
        'title' : 'Hello, state',
        'content' : 'Lorem ipsum dolor sit amet',
        'author' : 'John Doe'
    }
]


def list_blogs():
    return BLOGS


@app.route("/")
def hello_world():
  return render_template('main.html', filename='home.html', title="Home Page", blogs=BLOGS)

@app.route("/blogs")
def blogposts():
  return render_template('main.html', filename='allBlogs.html', title="Blogs")

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)


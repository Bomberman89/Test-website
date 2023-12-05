from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template('main.html', filename='home.html', title="Home Page")

@app.route("/blogs")
def blogposts():
  return render_template('main.html', filename='allBlogs.html', title="Blogs")

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)


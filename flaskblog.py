from flask import Flask, render_template

app = Flask(__name__)

posts = [
  {
    'title': 'Blog Post 1',
    'author': 'John Doe',
    'content': 'Blog post content 1',
    'date_posted': 'July 17, 2023'
  },
  {
    'title': 'Blog Post 2',
    'author': 'Jane Doe',
    'content': 'Blog post content 2',
    'date_posted': 'July 18, 2023'
  }
]


@app.route("/")
def home():
  return render_template('home.html', posts=posts)

@app.route('/about')
def about():
  return render_template('about.html', title='About')



if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
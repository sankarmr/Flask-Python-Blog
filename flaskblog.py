from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '8e06090c63e717df084ae5193cf21a02'

posts = [{
  'title': 'Blog Post 1',
  'author': 'John Doe',
  'content': 'Blog post content 1',
  'date_posted': 'July 17, 2023'
}, {
  'title': 'Blog Post 2',
  'author': 'Jane Doe',
  'content': 'Blog post content 2',
  'date_posted': 'July 18, 2023'
}]


@app.route("/")
def home():
  return render_template('home.html', posts=posts)


@app.route('/about')
def about():
  return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    flash(f"Account created for {form.username.data}!", 'success')
    return redirect(url_for('home'))
  return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'admin@blog.com' and form.password.data == 'password':
      flash('You have logged in successfully', 'success')
      return redirect(url_for('home'))
    else:
      flash('Login unsuccessful', 'danger')
  return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

from flask import Flask, render_template, url_for, redirect, flash
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '9b336e454dbb442f8264f8debb3af5d6'

myBlogs = [
        {
                'title':'Why Python',
                'content':'Python is High Level Programming Language',
                'author':'Onkar Nardekar',
                'timeStamp':'12th June, 2020'
        },
        {
                'title':'Top 2 Python Frameworks',
                'content':'Top 2 Python Framworks are Django and Flask Respectivily',
                'author':'Onkar Nardekar',
                'timeStamp':'13th June, 2020'
        },
       {
                'title':'Gym Abs workout',
                'content':'Abs workout is Very difficult, so leave it and Go buy some delicious Food to Eat, We all get one life so Enjoy',
                'author':'Onkar Nardekar',
                'timeStamp':'14th June, 2020'
        },
]

@app.route('/')
@app.route('/home')
def index():
        return render_template('blog/index.html', blogs=myBlogs)

@app.route('/login', methods=['GET','POST'])
def login():
        form = LoginForm()
        if form.validate_on_submit():
                flash(f'{form.username.data} You are Login Successfully', 'success')
                return redirect(url_for('index'))
        return render_template('user/login.html',form=form)

if __name__ == '__main__':
        app.run(debug=True)
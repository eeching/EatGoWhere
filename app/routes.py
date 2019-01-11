from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
	new_food = {'name': 'Wanton'}
	plan = [
		{
			'food': {'name': 'Steamboat'},
			'rating': 10
		},
		{
			'food': {'name': 'bbq'},
			'rating': 9
		}
	]
	return render_template('index.html', title ="Home", new_food=new_food, plan=plan)


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)

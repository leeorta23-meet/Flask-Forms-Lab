from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory fopr static files
)


username = "leeor"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]



@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')

	else: 
		username = request.form['username']
		password = request.form['password']
		return redirect(url_for('home'))
  
  
@app.route('/home', methods=['GET', 'POST'])  # '/' for the default page
def home():
  if request.method == 'GET':
  	return render_template('home.html', facebook_friends = facebook_friends)



@app.route('/friends_exists/<string:name>', methods=['GET', 'POST'])  # '/' for the default page
def friend_exist(name):
  if request.method == 'GET':
  	return render_template('friend_exists.html', name = name, friends = facebook_friends)




if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
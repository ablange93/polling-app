# import flask microservice. #
from flask import (
  Flask, render_template, request, flash, redirect, url_for, session
)

#import password hashing
from werkzeug.security import generate_password_hash, check_password_hash

# import data model. #
from models import db, Users


# initialize Flask object . #
votr = Flask(__name__)

# load config from the config file we created earlier. #
votr.config.from_object('config')

# initialize and create the database. #
db.init_app(votr)
db.create_all(app=votr)

@votr.route('/')
def home():
    return render_template('index.html')

@votr.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':
		
		# get the user details from the form 
		email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        
        # hash the password 
        password = generate_password_hash(password)
        
        # Instantiate a user object
        user = Users(email=email, username=username, password=password)
        
        #Add the user object to the database
        db.session.add(user)
		
		# SQLite database commit to save changes
		db.session.commit()
		
		flash('Thanks for signing up please login')
		
		return redirect(url_for('home'))
		
	# Then it's a GET request, just render the template	
	return render_template('signup.html')
	
@votr.route('/login', methods=['POST'])
def login():
	# we don't need to check the request type as flask will raise a bad request
    # error if a request aside from POST is made to this url
    
    username = request.form['username']
    password = request.form['password']
    
    # search the database for the User
    user = Users.query.filter_by(username=username).first()
    
    if user:
    	password_hash = user.password
    	
    	if check_password_hash(password_hash, password):
    		# The hash matches the password in the database log the user in
    		session['user'] = username
    		
    		flash('Login was succesfull')
    else:
    	# user wasn't found in the database
    	flash('Username or password is incorrect please try again', 'error')
    	
    return redirect(url_for('home'))
    	
    
if __name__ == '__main__':
    votr.run()
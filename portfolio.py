from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #This is the root
def index():
	return render_template('index.html')

@app.route('/projects')
def projects():
	return render_template('projects.html')

@app.route('/aboutMe')
def aboutMe():
	return render_template('aboutMe.html')

app.run(debug=True) #All routes go above THIS
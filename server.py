from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = "Rumplestiltskin"

@app.route('/')
def index():
	return render_template('index.html')

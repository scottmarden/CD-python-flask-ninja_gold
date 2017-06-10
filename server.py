from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = "Rumplestiltski"
import random
import datetime

locations = {"farm": [10, 20], "cave": [5, 10], "house": [2, 5], "casino": [0, 50]}


@app.route('/')
def index():
	if 'gold' not in session:
		session['gold'] = 10
	if 'activities' not in session:
		session['activities']=[]

	return render_template('index.html', money_bag=session['gold'], activities=session['activities'])

@app.route('/process_money', methods=['POST'])
def process_money():
	loc = request.form['building']
	range_start = locations[loc][0]
	range_end =	locations[loc][1]
	if loc == 'casino':
		flip = int(round(random.random()))
		print flip
		if flip == 1:
			#win money
			profit = random.randint(range_start, range_end)
			session['gold'] += profit
			action = "Entered a casino and won " + str(profit) + " gold .... Nice! " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			print action
		else:
			#lose money
			loss = random.randint(range_start, range_end)
			session['gold'] -= loss
			action = "Entered a casino and lost " + str(loss) + " gold .... Ouch. " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			print action
	else:
		profit = random.randint(range_start, range_end)
		session['gold'] += profit
		action = "Earned " + str(profit) + " gold from the " + loc + "! " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		print action
	session['activities'].append(str(action))
	print session['activities']

	return redirect('/')

@app.route("/reset", methods=['POST'])
def reset():
	session.clear()
	return redirect('/')


app.run(debug=True)

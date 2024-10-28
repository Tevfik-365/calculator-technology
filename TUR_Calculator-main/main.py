# Import
from flask import Flask, render_template, request




app = Flask(__name__)


def result_calculate(size, lights, device):
# Variables that allow to calculate the energy consumption of electrical devices
home_coef = 100
light_coef = 0.04
devices_coef = 5
return size * home_coef + lights * light_coef + device * devices_coef


# First page
@app.route('/')
def index():
return render_template('index.html')
# Second page
@app.route('/<size>')
def lights(size):
return render_template(
'lights.html',
size=size
)


# Page three
@app.route('/<size>/<lights>')
def electronics(size, lights):
return render_template(
'electronics.html',
size = size,
lights = lights
)


# Calculation
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
return render_template('end.html',
result=result_calculate(int(size),
int(lights),
int(device)
)
)
# Form
@app.route('/form')
def form():
return render_template('form.html')


#Results of the form
@app.route('/submit', methods=['POST'])
def submit_form():


name = request.form['name']
date = request.form['date']
address = request.form['address']
email = request.form['email']


with open('form.txt', 'a',) as f:
f.write(f "Name: { name} \n Email: { email} \n Address: { address} \n Gun: { date}" ' \n')


# You can save your data or send it by e-mail
return render_template('form_result.html',
# Place variables here
name=name,
date=date,
address=address,
email=email

from api1 import app
import json
import random


@app.route('/')
def home():
    return "<h1>Home Page</h1>"

@app.route('/ages')
def get_ages():
    ages = []
    for x in range(100):
        age = random.randint(1,101)
        ages.append(age)
    return json.dumps(ages)
# def random_number_generator()
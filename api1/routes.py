from api1 import app
import json
import random


@app.route('/')
def home():
    return "<h1>Home Page</h1>"

@app.route('/ages/<count>')
def get_ages(count):
    json_obj = {}
    # color = "steelblue"
    # json_obj["color"] = color
    points = []
    for x in range(int(count)):
        dict = {}
        key = x+1
        dict['x'] = key
        age = random.randint(1,101)
        dict["y"] = age
        points.append(dict)
        # dict[str(key)] = age
        # ages.append(dict)
    json_obj["points"] = points
    return json.dumps(points)
# def random_number_generator()
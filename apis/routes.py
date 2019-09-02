from apis import app
import json
import random


@app.route('/')
def home():
    return "<h1>Home Page</h1>"

@app.route('/temperature/<count>')
def get_temperature_values(count):
    json_data_points_obj = {}
    data_points = []
    for x in range(int(count)):
        data_point = {}

        key = x+1
        data_point['x'] = key
        temperature = random.randint(1,101)
        if(key%5==0):
            data_point["y"] = ''
        else:
            data_point["y"] = temperature
        data_points.append(data_point)
    json_data_points_obj["points"] = data_points
    return json.dumps(data_points)

@app.route('/speed/<count>')
def get_speed_values(count):
    json_data_points_obj = {}
    data_points = []
    for x in range(int(count)):
        data_point = {}

        key = x+1
        data_point['x'] = key
        temperature = random.randint(1,101)
        if(key%8==0):
            data_point["y"] = ''
        else:
            data_point["y"] = temperature
        data_points.append(data_point)
    json_data_points_obj["points"] = data_points
    return json.dumps(data_points)

@app.route('/fuel/<count>')
def get_fuel_values(count):
    json_data_points_obj = {}
    data_points = []
    for x in range(int(count)):
        data_point = {}

        key = x+1
        data_point['x'] = key
        temperature = random.randint(1,101)
        if(key%3==0):
            data_point["y"] = ''
        else:
            data_point["y"] = temperature
        data_points.append(data_point)
    json_data_points_obj["points"] = data_points
    return json.dumps(data_points)
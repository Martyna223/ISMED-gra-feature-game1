import requests
import json


# response = requests.get("http://127.0.0.1:5000/api/getdata")
# if response.status_code == 200:
#     print(response.json())

def post_data(d):
    d = json.dumps(d)
    response = requests.post("http://127.0.0.1:5000/api/setdata", data=d,
                             headers={'content-type': 'application/json'})

    if response.status_code == 201:
        print("Success!")

    return response.json()

def post_connect(id):
    data = {
        'i_am_here': True,
        'id': id,
    }
    print(data)
    return post_data(data)


id = 9999
response_connect = post_connect(id)
print(response_connect["prompt"])
# if (response_connect)

marker = 'x' # symulacja wpisania


def post_marker(id, marker):
    data = {
        'marker': marker,
        'id': id,
    }
    return post_data(data)

tile_id = 1


def post_tile(id, tile_id):
    data = {
        'tile_id': tile_id,
        'id': id,
    }
    return post_data(data)


response_marker = post_marker(id, marker)
print(response_marker)

print(post_tile(id, tile_id))
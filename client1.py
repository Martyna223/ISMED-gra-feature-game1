import requests
import json
import re


# response = requests.get("http://127.0.0.1:5000/api/getdata")
# if response.status_code == 200:
#     print(response.json())

def post_data(d):
    d = json.dumps(d)
    response = requests.post("http://127.0.0.1:5000/api/setdata", data=d,
                             headers={'content-type': 'application/json'})

    if response.status_code == 201:
        print("Success! You send: " + d)


    return response.json()

def post_connect(id):
    data = {
        'i_am_here': True,
        'id': id,
    }
    return post_data(data)


id = 3333
response_connect = post_connect(id)
print(response_connect)
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

def post_tile_id():
    tile_id = input("Please choose an unoccupied tile - from 1 to 9. ")
    num_format = re.compile(r'^[1-9]$')
    response1 = requests.get("http://127.0.0.1:5000/api/gettile")
    if re.match(num_format, tile_id):
        tile_id = int(tile_id) - 1
        if tile_id in response1.json():
            print("This tile is occupied.")
            post_tile_id()
        else:
            mydata1 = {'data': tile_id}
            d1 = json.dumps(mydata1)
            response = requests.post("http://127.0.0.1:5000/api/settile", data=d1,
                                 headers={'content-type': 'application/json'})
            if response.status_code == 201:
               print("Success!")
    else:
        print("This tile is not a valid symbol.")
        post_tile_id()


response_marker = post_marker(id, marker)
print(response_marker)

print(post_tile(id, tile_id))


post_tile_id()
post_tile_id()
post_tile_id()

response2 = requests.get("http://127.0.0.1:5000/api/gettile")
print(response2.json())

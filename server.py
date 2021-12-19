from flask import Flask, jsonify, request

app = Flask(__name__)

cache = {
    "players": {"player1": None, "player2": None},
    "markers": {},
    "current_tile": 0,
    "current_player": None,
}
tiles = []


@app.route("/")
def homepage():
    return "<html><body>Tic-tac-toe</body></html>"  # tu jest to co sie wyswietla dla uzytkownika


@app.route("/api/settile",methods=['POST'])
def settile():
    global  tiles
    data = request.get_json()
    if data is not None and 'data' in data:
        tiles.append(data['data'])
    return {}, 201


@app.route("/api/gettile",methods=['GET'])
def gettile():
    return jsonify(tiles), 200


@app.route("/api/setdata",methods=['POST'])
def setdata():
    global global_data
    data = request.get_json()
    response = None
    status = 201
    if data is not None:
        if 'i_am_here' in data:
            response = set_connect(data)

        elif 'marker' in data:
            response = set_marker(data)

        elif 'tile_id' in data:
            response = set_tile(data)

    return response, status


def set_connect(data):
    players = cache['players']
    if players['player1'] is None:
        players['player1'] = data['id']
        cache['current_player'] = players['player1']
        return {"prompt": "You're player 1!", "number": 1}
    elif players['player2'] is None:
        players['player2'] = data['id']
        return {"prompt": "You're player 2!", "number": 2}
    else:
        return {"prompt": "There already is a maximum number of players.", "number": 0}


def set_marker(data):
    players = cache['players']
    markers = cache['markers']
    if players['player1'] == data['id']:
        markers[players['player1']] = data['marker']
        markers[players['player2']] = 'o' if data['marker'] == 'x' else 'x'
        return {}


def set_tile(data):
    cache['current_tile'] = data['tile_id']
    switch_player()
    print(data)
    print(cache['current_tile'])
    return {}


def switch_player():
    players = cache['players']
    cache['current_player'] = players['player2'] if cache['current_player'] == players['player1'] else players['player1']
    print(cache['players'])


if __name__ == "__main__":
    app.run()


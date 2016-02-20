import bottle
import math
import os

SNAKE = 1
WALL = 2
FOOD = 3
GOLD = 4

def distance(p, q):
    dx = p[0] - q[0]
    dy = p[1] - q[1]
    return dx + dy;

def closest(items, start):
    closest_item = None
    closest_distance = 10000

    for item in items:
        item_distance = distance(start, item)
        if item_distance < closest_distance:
            closest_item = item
            closest_distance = item_distance

    return closest_item

def build_grid(data):
    grid = [[0 for col in xrange(data["width"])] for row in xrange(data["height"]]
    for snek in data["snakes"]:
        if snek["id "]== mysnake:
            mysnake = snek 
        for coord in snek["coords"]:
            grid[coord[0]][coord[1]] = SNAKE
    for wall in data["walls"]:
        grid[wall[0]][wall[1]] = WALL
    for g in data["gold"]:
        grid[g[0]][g[1]] = GOLD
    for f in data["food"]:
        grid[f[0]][f[1]] = FOOD

    return mysnake, grid

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
def index():
    head_url = '%s://%s/static/Traitor.gif' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    return {
        'color': '#00ff00',
        'head': head_url
    }


@bottle.post('/start')
def start():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'battlesnake-python!'
    }
# DATA OBJECT
# {
#     "game": "hairy-cheese",
#     "mode": "advanced",
#     "turn": 4,
#     "height": 20,
#     "width": 30,
#     "snakes": [
#         <Snake Object>, <Snake Object>, ...
#     ],
#     "food": [
#         [1, 2], [9, 3], ...
#     ],
#     "walls": [    // Advanced Only
#         [2, 2]
#     ],
#     "gold": [     // Advanced Only
#         [5, 5]
#     ]
# }

#SNAKE
# {
#     "id": "1234-567890-123456-7890",
#     "name": "Well Documented Snake",
#     "status": "alive",
#     "message": "Moved north",
#     "taunt": "Let's rock!",
#     "age": 56,
#     "health": 83,
#     "coords": [ [1, 1], [1, 2], [2, 2] ],
#     "kills": 4,
#     "food": 12,
#     "gold": 2
# }

@bottle.post('/move')
def move():
    mysnakeid = "de508402-17c8-4ac7-ab0b-f96cb53fbee8"
    data = bottle.request.json

    snek, grid = build_grid(data)
    closest_goal = closest(data["food"] + data["gold"])

    return {
        'move': 'north',
        'taunt': 'TRAITOR!'
    }


@bottle.post('/end')
def end():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'battlesnake-python!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))

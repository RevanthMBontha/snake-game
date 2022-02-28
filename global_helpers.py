import random

# Snake related const values
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_COLORS = ['gray90', 'honeydew', 'ivory', 'lemonchiffon', 'lavender', 'OldLace', 'MintCream',
                'PapayaWhip', 'WhiteSmoke', 'seashell', 'snow1', 'moccasin']
RANDOM_COLORS = ['bisque3', 'blue', 'BlueViolet', 'brown', 'burlywood', 'CadetBlue1', 'chartreuse', 'chocolate', 'cyan',
                 'DarkGoldenrod1', 'DarkGreen', 'DarkMagenta', 'DarkOrange1', 'DarkOrchid1', 'DeepPink1', 'DarkRed']
MOVE_DISTANCE = 20
SNAKE_COMPRESS_RATIO = 1

# Directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Food Related stuff
SPAWN_LOWER_LIMIT = -250
SPAWN_UPPER_LIMIT = 250

FOOD_COLORS = ['maroon1', 'MediumSpringGreen', 'orchid', 'yellow1', 'GreenYellow',
               'LightSeaGreen', 'tomato', 'turquoise1', 'VioletRed', 'YellowGreen',
               'purple1', 'orange', 'OliveDrab1', 'OrangeRed', 'PaleGreen', 'LawnGreen',
               'gold1', 'HotPink', 'LightCoral']

# Scoreboard related stuff
FONT = 'Courier'
ALIGNMENT = 'center'

# Main Related Stuff
GAME_REFRESH_RATE = 1 / 10
CONTACT_THRESHOLD = 15


# Helper Functions
def get_random_location():
    """Returns a random location in a range"""
    random_x = random.randint(SPAWN_LOWER_LIMIT, SPAWN_UPPER_LIMIT)
    random_y = random.randint(SPAWN_LOWER_LIMIT, SPAWN_UPPER_LIMIT)
    return random_x, random_y


def get_random_color(_choices):
    """Returns a random color from a list of colors"""
    return random.choice(_choices)

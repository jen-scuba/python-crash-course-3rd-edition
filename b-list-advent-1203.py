# https://www.b-list.org/weblog/2023/dec/03/python-enums/

import enum
class Direction(enum.Enum):
    NORTH = "north"
    EAST = "east"
    SOUTH = "south"
    WEST = "west"
    
class Status(enum.Enum):
    DRAFT = 0
    PUBLISHED = 1
    HIDDEN = 2
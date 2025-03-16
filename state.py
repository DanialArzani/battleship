from enum import Enum

class State(Enum):
    WATER = 0
    SMALL_SHIP = 1
    MEDIUM_SHIP = 2
    BIG_SHIP = 3
    TREASURE = 4
    DESTROYED_SHIP = 5
    MISSED_SHOT = 6


#State = Enum('State',[('WATER',0),('SMALL_SHIP',1),('MEDIUM_SHIP',2),('BIG_SHIP',3),('TREASURE',4)])

s = State
print(s(2).name)

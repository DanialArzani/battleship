from enum import Enum


class  WaterState(Enum):
    WATER = 0
    SMALL_SHIP = 1
    MEDIUM_SHIP = 2
    BIG_SHIP = 3
    TREASURE = 4
    DESTROYED_SHIP = 5
    MISSED_SHOT = 6

    
#State = Enum('State',[('WATER',0),('SMALL_SHIP',1),('MEDIUM_SHIP',2),('BIG_SHIP',3),('TREASURE',4)])

State = WaterState
print(State(2).name)
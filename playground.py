from raylib import *
from state import State

class Playground:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = [[0 for _ in range(width)] for _ in range(height)]
        create()

    # initialize
    def create():
        for row in range(height):
            for section in range(width):
                water_block = self.matrix[row][section]
                water_block = State(water_block) 
        pass

    def draw():
        pass

from pyray import *
from state import State

class Playground:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = [[0 for _ in range(width)] for _ in range(height)]
        self.create()
        # loading assets
        image = load_image("assets/sprites/water.png")
        if image.width == 0 or image.height == 0:
            print("Failed to load image")
            close_window()
            return

        self.water_texture = load_texture_from_image(image)
        unload_image(image)

    # initialize
    def create(self):
        for row in range(self.height):
            for col in range(self.width):
                self.matrix[row][col] = State.WATER

    def draw(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.matrix[row][col] == State.WATER:
                    draw_texture(self.water_texture , col*16, row*16, WHITE)        
        pass

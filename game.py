import globs
from pyray import *
from playground import Playground

class Game:
    def init(self):
        init_window(globs.WIDTH, globs.HEIGHT, "BattleShip")
        self.playground = Playground(10, 10)

    def loop(self):
        while not window_should_close():
            begin_drawing()
            clear_background(WHITE)
            self.playground.draw()
            end_drawing()

    def destroy(self):
        close_window()
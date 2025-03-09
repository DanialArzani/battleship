import globs
from pyray import *

class Menu:
    def init(self):
        init_window(globs.WIDTH, globs.HEIGHT, "BattleShip")

    def loop(self):
        while not window_should_close():
            begin_drawing()
            clear_background(WHITE)
            draw_text("BattleShip", int(globs.WIDTH / 2) - 90, int(globs.HEIGHT / 2) - 10, 40, VIOLET)
            end_drawing()

    def destroy(self):
        close_window()
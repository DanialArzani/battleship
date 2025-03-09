from pyray import *

WIDTH = 1000
HEIGHT = 1000

init_window(WIDTH, HEIGHT, "BattleShip")

while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    draw_text("BattleShip", int(WIDTH / 2) - 90, int(HEIGHT / 2) - 10, 40, VIOLET)
    end_drawing()

close_window()
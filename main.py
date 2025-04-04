from pyray import *
import menu
import game

currentScene = game.Game()

def main():
    currentScene.init()
    currentScene.loop()
    currentScene.destroy()

if __name__ == '__main__':
    main()

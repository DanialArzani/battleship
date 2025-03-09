from pyray import *
import menu

currentScene = menu.Menu()

def main():
    currentScene.init()
    currentScene.loop()
    currentScene.destroy()

if __name__ == '__main__':
    main()
from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    m1 = Maze(150, 50, 10, 10, 50, 50, win)
    m1.solve()
    win.wait_for_close()
    

if __name__ == "__main__":
    main()
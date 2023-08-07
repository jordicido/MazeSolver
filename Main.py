from Maze import Maze
from Window import Window


def main():
    win = Window(1800, 1400, "Maze Solver")
    maze = Maze(10, 10, 10, 10, 100, 100, win, 50)
    maze.solve()
    win.wait_for_close()

main()
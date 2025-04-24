from tkinter import Tk, BOTH, Canvas
from line import Line, Point
from cell import Cell
from maze import Maze

# Class to handle the GUI
class Window():
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True

        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)


def main():
    try:
        win = Window(825, 625)

        maze = Maze(
            5,          # x1: left edge
            10,          # y1: top edge
            8,          # num_rows
            10,         # num_cols
            80,         # cell_size_x
            75,         # cell_size_y
            win         # win object
        )
        maze._break_entrance_and_exit()
        maze._break_walls_r(0, 0)

        maze.solve()

        win.wait_for_close()
        
        
    finally:
        print("Window has been closed. Goodbye!")

main()
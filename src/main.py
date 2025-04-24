from tkinter import Tk, BOTH, Canvas
from line import Line, Point
from cell import Cell

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
        win = Window(800, 600)

        cell_1 = Cell(50, 100, 50, 100, win)
        cell_1.draw(cell_1._x1, cell_1._y1, cell_1._x2, cell_1._y2)

        # Example 2: Remove the top wall
        cell_2 = Cell(120, 180, 50, 100, win)  # A cell to the right of the first
        cell_2.has_top_wall = False
        cell_2.draw(cell_2._x1, cell_2._y1, cell_2._x2, cell_2._y2)

        # Example 3: Remove the left and bottom walls
        cell_3 = Cell(50, 100, 120, 170, win)  # A cell below the first
        cell_3.has_left_wall = False
        cell_3.has_bottom_wall = False
        cell_3.draw(cell_3._x1, cell_3._y1, cell_3._x2, cell_3._y2)

        # Example 4: A cell with only the right wall
        cell_4 = Cell(120, 180, 120, 170, win)
        cell_4.has_left_wall = False
        cell_4.has_top_wall = False
        cell_4.has_bottom_wall = False
        cell_4.draw(cell_4._x1, cell_4._y1, cell_4._x2, cell_4._y2)
        
        win.wait_for_close()
        
        
    finally:
        print("Window has been closed. Goodbye!")

main()
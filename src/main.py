from tkinter import Tk, BOTH, Canvas
from line import Line, Point

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

        point1 = Point(10, 10)
        point2 = Point(100, 100)
        line = Line(point1, point2)

        point3, point4 = Point(54, 85), Point(33, 55)
        second_line = Line(point3, point4)

        win.draw_line(line, "purple")
        win.draw_line(second_line, "yellow")
        win.wait_for_close()
        
        
    finally:
        print("Window has been closed. Goodbye!")

main()
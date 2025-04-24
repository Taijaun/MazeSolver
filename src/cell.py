from tkinter import Canvas
from line import Line, Point

class Cell():
    def __init__(self, x1, x2, y1, y2, win=None):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, top_left_x, top_left_y, bottom_right_x, bottom_right_y):
        if not self._win:
            return
        
        left_wall = Line(Point(top_left_x, top_left_y), Point(top_left_x, bottom_right_y))
        if self.has_left_wall:
            self._win.draw_line(left_wall, "purple")
        else:
            self._win.draw_line(left_wall, "white")
        
        right_wall = Line(Point(bottom_right_x, top_left_y), Point(bottom_right_x, bottom_right_y))
        if self.has_right_wall:
            self._win.draw_line(right_wall, "purple")
        else:
            self._win.draw_line(right_wall, "white")

        top_wall = Line(Point(top_left_x, top_left_y), Point(bottom_right_x, top_left_y))
        if self.has_top_wall:
            self._win.draw_line(top_wall, "purple")
        else:
            self._win.draw_line(top_wall, "white")

        bottom_wall = Line(Point(top_left_x, bottom_right_y), Point(bottom_right_x, bottom_right_y))
        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall, "purple")
        else:
            self._win.draw_line(bottom_wall, "white")

    def draw_move(self, to_cell, undo=False):
        fill = ""

        if undo:
            fill = "gray"
        else:
            fill = "red"

        # Current cell center
        center_x = (self._x1 + self._x2) / 2
        center_y = (self._y1 + self._y2) / 2

        # destination cell center
        to_x = (to_cell._x1 + to_cell._x2) / 2
        to_y = (to_cell._y1 + to_cell._y2) / 2

        # Create the line
        line = Line(Point(center_x, center_y), Point(to_x, to_y))
        if self.win:
            self._win.draw_line(line, fill)

        

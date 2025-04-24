from cell import Cell
import time

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []

        for _ in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                new_cell = Cell(0, 0, 0, 0, self.win)
                column.append(new_cell)
            self._cells.append(column)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        # Calc coords based on maze position
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        # Update cell coords
        cell = self._cells[i][j]
        cell._x1 = x1
        cell._x2 = x2
        cell._y1 = y1
        cell._y2 = y2
        cell.draw(x1, y1, x2, y2)

        self._animate()

    def _animate(self):
        if self.win:
            self.win.redraw()
            time.sleep(0.05)
        
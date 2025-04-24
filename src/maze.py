import random
import time
from cell import Cell


class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed = None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = seed
        if self.seed:
            random.seed(seed)
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

    def _break_entrance_and_exit(self):
        # Break top wall of entrance cell
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        self._draw_cell(0, 0)

        # Break the bottom wall of exit cell
        exit_cell = self._cells[self.num_cols-1][self.num_rows-1]
        exit_cell.has_bottom_wall = False
        self._draw_cell(self.num_cols-1, self.num_rows-1)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True

        while True:
            # Empty list for unvisted neighbours
            directions = []
        
        # check the cell above
            if j > 0 and not self._cells[i][j-1].visited:
                directions.append((i, j-1))

            # Check cell below
            if j < self.num_rows - 1 and not self._cells[i][j+1].visited:
                directions.append((i, j+1))

            # Check cell to the left
            if i > 0 and not self._cells[i-1][j].visited:
                directions.append((i-1, j))

            # Check cell to the right
            if i < self.num_cols - 1 and not self._cells[i+1][j].visited:
                directions.append((i+1, j))

            
            # If no unvisted neighbors
            if len(directions) == 0:
                self._draw_cell(i, j)
                return
            
            # chose a random direction
            next_i, next_j = directions[random.randrange(len(directions))]

            # Break down walls
            if next_i == i and next_j == j - 1: # Up
                current_cell.has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            elif next_i == i and next_j == j + 1: # Down
                current_cell.has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False
            elif next_i == i - 1 and next_j == j: # Left
                current_cell.has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
            elif next_i == i + 1 and next_j == j: # Right
                current_cell.has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False

            # Draw currentcell with walls removed
            self._draw_cell(i, j)

            self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False



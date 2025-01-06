from cell import Cell
import time

class Maze:
    def __init__(
        self,
        x,
        y,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
    
    def _create_cells(self):
        for col in range(self._num_cols):
            current = []
            for row in range(self._num_rows):
                current.append(Cell(self._win))
            self._cells.append(current)
        
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cells(col, row)

    def _draw_cells(self, i, j):
            self._cells[i][j].set_pos(self._x + (i * self._cell_size_x), self._x + ((i + 1) * self._cell_size_x),
                                       self._y + (j * self._cell_size_y), self._y + ((j + 1) * self._cell_size_y))
            self._cells[i][j].draw()
            self._animate()

    def _animate(self):
        time.sleep(.05)
    
    def get_cells(self):
        return self._cells
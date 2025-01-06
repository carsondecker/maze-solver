from cell import Cell
import time
import random

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
        seed=None
    ):
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed != None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r()
        self._reset_cells_visited()

    def _create_cells(self):
        for col in range(self._num_cols):
            current = []
            for row in range(self._num_rows):
                current.append(Cell(self._win))
            self._cells.append(current)
        
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].set_pos(self._x + (i * self._cell_size_x) + i, self._x + ((i + 1) * self._cell_size_x) + i,
                                       self._y + (j * self._cell_size_y) + j, self._y + ((j + 1) * self._cell_size_y) + j)
                self._draw_cells(i, j)

    def _draw_cells(self, i, j):
            self._cells[i][j].draw()
            self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw()
        self._cells[len(self._cells) - 1][len(self._cells[0]) - 1].has_bottom_wall = False
        self._cells[len(self._cells) - 1][len(self._cells[0]) - 1].draw()
    
    def _break_walls_r(self, i=0, j=0):
        self._cells[i][j].visited = True
        while True:
            unvisited = []
            if i != 0:
                if not self._cells[i - 1][j].visited:
                    unvisited.append([i - 1, j])
            if j != 0:
                if not self._cells[i][j - 1].visited:
                    unvisited.append([i, j - 1])
            if i != len(self._cells) - 1:
                if not self._cells[i + 1][j].visited:
                    unvisited.append([i + 1, j])
            if j != len(self._cells[0]) - 1:
                if not self._cells[i][j + 1].visited:
                    unvisited.append([i, j + 1])
            
            if len(unvisited) == 0:
                return
            next_cell = unvisited[random.randint(0, len(unvisited) - 1)]
            self._break_walls_between(self._cells[i][j], self._cells[next_cell[0]][next_cell[1]])
            self._cells[i][j].draw()
            self._cells[next_cell[0]][next_cell[1]].draw()
            self._animate()
            self._break_walls_r(next_cell[0], next_cell[1])
    
    def _break_walls_between(self, cell1, cell2):
        if cell1._x1 < cell2._x1:
            cell1.has_right_wall = False
            cell2.has_left_wall = False
        elif cell1._y1 < cell2._y1:
            cell1.has_bottom_wall = False
            cell2.has_top_wall = False
        elif cell1._x1 > cell2._x1:
            cell1.has_left_wall = False
            cell2.has_right_wall = False
        else:
            cell1.has_top_wall = False
            cell2.has_bottom_wall = False

    def _reset_cells_visited(self):
        for cell_list in self._cells:
            for cell in cell_list:
                cell.visited = False
    
    def solve(self):
        self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        
        if i == len(self._cells) - 1 and j == len(self._cells[0]) - 1:
            return True
        
        unvisited = []
        if i != 0 and not self._cells[i][j].has_left_wall and not self._cells[i - 1][j].visited:
            unvisited.append([i - 1, j])
        if j != 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j - 1].visited:
            unvisited.append([i, j - 1])
        if i != len(self._cells) - 1 and not self._cells[i][j].has_right_wall and not self._cells[i + 1][j].visited:
            unvisited.append([i + 1, j])
        if j != len(self._cells[0]) - 1 and not self._cells[i][j].has_bottom_wall and not self._cells[i][j + 1].visited:
            unvisited.append([i, j + 1])
        
        for cell in unvisited:
            self._cells[i][j].draw_move(self._cells[cell[0]][cell[1]])
            if self._solve_r(cell[0], cell[1]):
                return True
            self._cells[i][j].draw_move(self._cells[cell[0]][cell[1]], undo=True)
        return False
        
import unittest
from maze import Maze
from window import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        win = Window(800, 600)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_draw_cells(self):
        num_cols = 2
        num_rows = 2
        win = Window(800, 600)
        m1 = Maze(10, 10, num_rows, num_cols, 10, 10, win)
        self.assertEqual(m1._cells[0][0]._x1, 10)
        self.assertEqual(m1._cells[0][0]._y1, 10)
        self.assertEqual(m1._cells[1][0]._x1, 20)
        self.assertEqual(m1._cells[1][0]._y1, 10)
        self.assertEqual(m1._cells[0][1]._x1, 10)
        self.assertEqual(m1._cells[0][1]._y1, 20)
        self.assertEqual(m1._cells[1][1]._x1, 20)
        self.assertEqual(m1._cells[1][1]._y1, 20)

if __name__ == "__main__":
    unittest.main()
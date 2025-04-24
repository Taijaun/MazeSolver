import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_small(self):
        num_cols = 5
        num_rows = 3
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 25
        num_rows = 30
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_break_entrance_and_exit(self):
        # Setup
        maze = Maze(0, 0, 3, 3, 10, 10)
    
        # Before breaking walls, confirm they exist
        self.assertTrue(maze._cells[0][0].has_top_wall)
        self.assertTrue(maze._cells[2][2].has_bottom_wall)
    
        # Break entrance and exit
        maze._break_entrance_and_exit()
    
        # Verify walls were broken
        self.assertFalse(maze._cells[0][0].has_top_wall)
        self.assertFalse(maze._cells[2][2].has_bottom_wall)
    
    def test_reset_cells_visited(self):
        # Create a small test maze (no window needed for testing)
        test_maze = Maze(0, 0, 3, 3, 10, 10, win=None)
        
        # Mark some cells as visited
        test_maze._cells[0][0].visited = True
        test_maze._cells[1][1].visited = True
        test_maze._cells[2][2].visited = True
        
        # Verify that those cells are indeed marked as visited
        self.assertTrue(test_maze._cells[0][0].visited)
        self.assertTrue(test_maze._cells[1][1].visited)
        self.assertTrue(test_maze._cells[2][2].visited)
        
        # Call the method we're testing
        test_maze._reset_cells_visited()
        
        # Verify all cells have visited=False
        for i in range(3):
            for j in range(3):
                self.assertFalse(test_maze._cells[i][j].visited, 
                                f"Cell at [{i}][{j}] should not be visited")

if __name__ == "__main__":
    unittest.main()
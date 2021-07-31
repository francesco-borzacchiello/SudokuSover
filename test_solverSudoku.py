import unittest

from sudoku import * 
from sudokuSolver import *

class TestSudokuSolver(unittest.TestCase):
    
    def setUp(self):
        print()

    def __solve_sudoku(self, sudoku : ClassicSudoku, solution : ClassicSudoku):
        solver = ClassicSudokuSolver(sudoku)
        solver.solve()
        self.assertEqual(solver.get_solution(), solution)

    # base case resolvable with the method of the single candidate in a cell
    def test_solve_sudoku_4x4_cell_with_one_candidate(self):
        sudoku = ClassicSudoku([[2, 0, 4, 0],
                                [0, 0, 0, 0],
                                [1, 0, 0, 3],
                                [3, 2, 1, 0]])
        
        solution = ClassicSudoku([[2, 3, 4, 1],
                                [4, 1, 3, 2],
                                [1, 4, 2, 3],
                                [3, 2, 1, 4]])

        self.__solve_sudoku(sudoku, solution)

    # sudoku resolvable with the method of the candidate with only one occurence in one row
    def test_solve_sudoku_9x9_candidate_with_only_one_occurrence_in_row(self):
        sudoku = ClassicSudoku([[0, 8, 3, 1, 0, 9, 0, 0, 0],
                                [0, 0, 0, 0, 0, 3, 5, 0, 0],
                                [4, 6, 0, 7, 0, 0, 0, 0, 1],
                                [0, 0, 4, 6, 0, 0, 0, 0, 0],
                                [3, 9, 0, 0, 0, 0, 7, 5, 0],
                                [0, 0, 0, 0, 0, 7, 0, 4, 3],
                                [0, 0, 0, 0, 8, 6, 9, 0, 0],
                                [0, 3, 7, 0, 4, 2, 6, 1, 5],
                                [6, 2, 9, 0, 7, 1, 0, 3, 8]])
        
        solution = ClassicSudoku([[7, 8, 3, 1, 5, 9, 2, 6, 4],
                                    [9, 1, 2, 4, 6, 3, 5, 8, 7],
                                    [4, 6, 5, 7, 2, 8, 3, 9, 1],
                                    [1, 7, 4, 6, 3, 5, 8, 2, 9],
                                    [3, 9, 8, 2, 1, 4, 7, 5, 6],
                                    [2, 5, 6, 8, 9, 7, 1, 4, 3],
                                    [5, 4, 1, 3, 8, 6, 9, 7, 2],
                                    [8, 3, 7, 9, 4, 2, 6, 1, 5],
                                    [6, 2, 9, 5, 7, 1, 4, 3, 8]])

        self.__solve_sudoku(sudoku, solution)

    def test_solve_second_sudoku_9x9_candidate_with_only_one_occurrence_in_row(self):
        sudoku = ClassicSudoku([[0, 0, 0, 0, 0, 0, 0, 8, 3],
                                [0, 0, 0, 2, 6, 7, 4, 0, 0],
                                [0, 0, 0, 0, 0, 3, 6, 0, 0],
                                [7, 6, 0, 5, 0, 0, 2, 0, 0],
                                [0, 1, 0, 0, 0, 0, 0, 9, 0],
                                [0, 0, 8, 0, 0, 9, 7, 4, 5],
                                [8, 0, 2, 3, 0, 0, 0, 0, 0],
                                [0, 0, 4, 9, 8, 6, 0, 0, 0],
                                [1, 9, 0, 0, 0, 0, 0, 0, 0]])
        
        solution = ClassicSudoku([[6, 2, 7, 1, 9, 4, 5, 8, 3],
                                    [5, 8, 3, 2, 6, 7, 4, 1, 9],
                                    [9, 4, 1, 8, 5, 3, 6, 2, 7],
                                    [7, 6, 9, 5, 4, 8, 2, 3, 1],
                                    [4, 1, 5, 7, 3, 2, 8, 9, 6],
                                    [2, 3, 8, 6, 1, 9, 7, 4, 5],
                                    [8, 5, 2, 3, 7, 1, 9, 6, 4],
                                    [3, 7, 4, 9, 8, 6, 1, 5, 2],
                                    [1, 9, 6, 4, 2, 5, 3, 7, 8]])

        self.__solve_sudoku(sudoku, solution)

    if __name__ == '__main__':
        unittest.main()
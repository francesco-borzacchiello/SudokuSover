""" 
reference: https://www.smartersudoku.com/

.---.---.---.
|...|...|.83|
|...|267|4..|
|...|..3|6..|
:--- --- ---:
|76.|5..|2..|
|.1.|...|.9.|
|..8|..9|745|
:--- --- ---:
|8.2|3..|...|
|..4|986|...|
|19.|...|...|
'---'---'---' 

0 0 0 | 0 0 0 | 0 8 3
0 0 0 | 2 6 7 | 4 0 0 
0 0 0 | 0 0 3 | 6 0 0 
---------------------
7 6 0 | 5 0 0 | 2 0 0 
0 1 0 | 0 0 0 | 0 9 0 
0 0 8 | 0 0 9 | 7 4 5
---------------------
8 0 2 | 3 0 0 | 0 0 0 
0 0 4 | 9 8 6 | 0 0 0 
1 9 0 | 0 0 0 | 0 0 0 

___________________________________________________________________________

.---.---.---.
|.83|1.9|...|
|...|..3|5..|
|46.|7..|..1|
:--- --- ---:
|..4|6..|...|
|39.|...|75.|
|...|..7|.43|
:--- --- ---:
|...|.86|9..|
|.37|.42|615|
|629|.71|.38|
'---'---'---'
"""

from sudoku import * 
from sudokuSolver import *

# Refer to testing, main should be empty at the moment

""" sudoku = ClassicSudoku([[2, 0, 4, 0],
                        [0, 0, 0, 0],
                        [1, 0, 0, 3],
                        [3, 2, 1, 0]]) """

""" sudoku = ClassicSudoku([[0, 0, 0, 0, 0, 0, 0, 8, 3],
                        [0, 0, 0, 2, 6, 7, 4, 0, 0],
                        [0, 0, 0, 0, 0, 3, 6, 0, 0],
                        [7, 6, 0, 5, 0, 0, 2, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 9, 0],
                        [0, 0, 8, 0, 0, 9, 7, 4, 5],
                        [8, 0, 2, 3, 0, 0, 0, 0, 0],
                        [0, 0, 4, 9, 8, 6, 0, 0, 0],
                        [1, 9, 0, 0, 0, 0, 0, 0, 0]]) """

""" sudoku = ClassicSudoku([[0, 8, 3, 1, 0, 9, 0, 0, 0],
                        [0, 0, 0, 0, 0, 3, 5, 0, 0],
                        [4, 6, 0, 7, 0, 0, 0, 0, 1],
                        [0, 0, 4, 6, 0, 0, 0, 0, 0],
                        [3, 9, 0, 0, 0, 0, 7, 5, 0],
                        [0, 0, 0, 0, 0, 7, 0, 4, 3],
                        [0, 0, 0, 0, 8, 6, 9, 0, 0],
                        [0, 3, 7, 0, 4, 2, 6, 1, 5],
                        [6, 2, 9, 0, 7, 1, 0, 3, 8]]) """

sudoku = ClassicSudoku([[0, 3, 0, 0, 0, 1, 0, 0, 9],
                        [9, 4, 0, 2, 0, 0, 0, 7, 0],
                        [0, 0, 0, 9, 0, 0, 2, 0, 0],
                        [3, 0, 0, 5, 7, 0, 0, 0, 8],
                        [0, 0, 0, 1, 0, 8, 0, 0, 0],
                        [5, 0, 0, 0, 4, 6, 0, 0, 7],
                        [0, 0, 5, 0, 0, 9, 0, 0, 0],
                        [0, 9, 0, 0, 0, 4, 0, 8, 2],
                        [1, 0, 0, 8, 0, 0, 0, 3, 0]])                        

ClassicSudokuSolver(sudoku).solve()
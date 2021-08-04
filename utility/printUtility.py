from numpy import *

from puzzle.cell import *
from puzzle.sudoku import ClassicSudoku

class PrintClassicSudokuBoard:
    def __init__(self, sudoku : ClassicSudoku):
        self.__sudoku = sudoku
        self.__board = ""

    def make_top_frame(self) -> str:
        return self.__make_frame_parts("╔", "═", "╦", "╗\n")
    
    def __make_orizontal_divider_frame(self) -> str:
        return self.__make_frame_parts("╠", "═", "╬", "╣\n")

    def make_bottom_frame(self) -> str:
        return self.__make_frame_parts("╚", "═", "╩", "╝\n")

    def __make_frame_parts(self, start: str, edge: str, divider : str, end : str) -> str:
        return self.__make_frame_parts_with_additional_divider(start, edge, divider, edge, end)

    def __make_orizontal_divider_block(self) -> str:
        return self.__make_frame_parts_with_additional_divider("║", "─", "║", "┼", "║\n")

    def __make_frame_parts_with_additional_divider(self, start: str, edge: str, divider : str,
                                                    intermediate_divider : str, end : str) -> str:
        # + 2 for aesthetic reasons, to increase the width of the sudoku  
        border_cell = edge * (self.__sudoku.values_for_side_of_a_block + 2)
        border_block = (((border_cell + intermediate_divider) 
                         * (self.__sudoku.values_for_side_of_a_block - 1))
                        + border_cell)
        return (start 
                + ((border_block + divider) * (self.__sudoku.blocks_for_side_of_a_sudoku - 1)) 
                + border_block
                + end)

    def make_board(self, candidates : dict) -> str:
        for row in range(self.__sudoku.values_for_side_of_a_sudoku):
            self.__make_row_of_a_board(row, candidates)
            self.__make_orizontal_divider(row)
        return self.__board
    
    def __make_row_of_a_board(self, row : int, candidates : dict):
        for row_of_value in range(self.__sudoku.values_for_side_of_a_block):
                self.__board += "║ "
                self.__make_contents_of_a_row_of_a_board(row, row_of_value, candidates)
                self.__board += " ║\n"
    
    def __make_contents_of_a_row_of_a_board(self, row : int, row_of_value : int, candidates : dict):
        for column in range(self.__sudoku.values_for_side_of_a_sudoku):
            for column_of_value in range(self.__sudoku.values_for_side_of_a_block):
                cell = IndicesOfCell(row, column)
                self.__make_the_part_of_a_single_cell(cell, IndicesOfCell(row_of_value, column_of_value),
                                                        self.__sudoku.get_the_value_from_cell(cell), candidates)
               
    def __make_the_part_of_a_single_cell(self, cell : IndicesOfCell, part_of_cell : IndicesOfCell, value : int, candidates : dict):
        self.__make_the_content_of_a_part_of_a_single_cell(cell, part_of_cell, value, candidates)
        self.__board += self.__make_vertical_divider_frame(cell.column, part_of_cell.column)

    def __make_the_content_of_a_part_of_a_single_cell(self, cell : IndicesOfCell, part_of_cell : IndicesOfCell,
                                                        value : int, candidates : dict):
        if value != 0:
            self.__board += self.__make_cell_full(part_of_cell, value)
        else:
            self.__make_the_part_of_a_single_cell_with_candidates(
                candidates[cell], 
                self.__calculate_expected_candidate(part_of_cell))

    def __make_vertical_divider_frame(self, column : int, column_of_cell : int) -> str:
        if (column_of_cell == self.__sudoku.values_for_side_of_a_block - 1 
            and (column + 1) % self.__sudoku.values_for_side_of_a_block != 0
            and column != (self.__sudoku.values_for_side_of_a_sudoku) - 1):
                return " │ "
        elif (column_of_cell == self.__sudoku.values_for_side_of_a_block - 1 
              and(column + 1) % self.__sudoku.values_for_side_of_a_block == 0
              and column != (self.__sudoku.values_for_side_of_a_sudoku) - 1):
                return " ║ "
        return ""

    def __make_cell_full(self, cell : IndicesOfCell, value : int) -> str:
        if (cell.row == (cell.column % self.__sudoku.blocks_for_side_of_a_sudoku) 
            and int(self.__sudoku.blocks_for_side_of_a_sudoku / 2) == cell.row):
                return str(value)
        return "•"

    def __make_the_part_of_a_single_cell_with_candidates(self, candidates : list, expected_candidate : int):
        if expected_candidate in candidates:
            self.__board += str(expected_candidate)
        else:
            self.__board += " "

    def __calculate_expected_candidate(self, part_of_cell : IndicesOfCell) -> int:
        return (part_of_cell.row * self.__sudoku.values_for_side_of_a_block) + (part_of_cell.column + 1)

    def __make_orizontal_divider(self, row : int):
        if row + 1 != (self.__sudoku.blocks_for_side_of_a_sudoku * self.__sudoku.values_for_side_of_a_block):
            if (row + 1) % self.__sudoku.values_for_side_of_a_block == 0:
                self.__board += self.__make_orizontal_divider_frame()
            else:
                self.__board += self.__make_orizontal_divider_block()
# https://leetcode.com/problems/valid-sudoku/description/
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# "." is unfilled
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
class ValidSudoku:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_to_nums = collections.defaultdict(set)
        col_to_nums = collections.defaultdict(set)
        box_to_nums = collections.defaultdict(set)
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if (
                    val in row_to_nums[row] or
                    val in col_to_nums[col] or
                    val in box_to_nums[(row // 3, col // 3)]
                ):
                    return False
                if val == ".":
                    continue

                row_to_nums[row].add(val)
                col_to_nums[col].add(val)
                box_to_nums[(row // 3, col // 3)].add(val)

        return True

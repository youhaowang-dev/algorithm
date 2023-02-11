# Array, Backtracking, Matrix
# https://leetcode.com/problems/word-search/

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
# or vertically neighboring. The same letter cell may not be used more than once.

# time O(m*n*3^k), k=len(word) and m and n are sizes of our board, max search depth is k and each search can branch 3 searches
# space k
class WordSearch:
    USED = "USED"

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                current_word = ""
                if self.has_word(board, word, row, col, current_word):
                    return True

        return False

    def has_word(self, board, word, row, col, current_word):
        if current_word == word:
            return True

        if (
            row < 0 or
            row >= len(board) or
            col < 0 or
            col >= len(board[0])
        ):
            return False

        char = board[row][col]
        if char == self.USED:
            return False

        for row_delta, col_delta in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_row = row + row_delta
            next_col = col + col_delta

            board[row][col] = self.USED
            if self.has_word(board, word, next_row, next_col, current_word + char):
                return True
            board[row][col] = char

        return False

# Array, Backtracking, Matrix
# https://leetcode.com/problems/word-search/

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
# or vertically neighboring. The same letter cell may not be used more than once.

# time O(m*n*3^k), k=len(word) and m and n are sizes of our board, max search depth is k and each search can branch 3 searches
# space k
class WordSearch:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0] or not word:
            return False

        row_count = len(board)
        col_count = len(board[0])
        used = set()

        def has_word(row, col, word_index):
            # if order matters
            if word_index == len(word):
                return True

            if not (
                0 <= row < row_count and
                0 <= col < col_count
            ):
                return False

            if (row, col) in used:
                return False

            if board[row][col] != word[word_index]:
                return False

            used.add((row, col))
            for row_delta, col_delta in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if has_word(row + row_delta, col + col_delta, word_index + 1):
                    return True
            used.remove((row, col))

        for row in range(row_count):
            for col in range(col_count):
                if has_word(row, col, 0):
                    return True

        return False

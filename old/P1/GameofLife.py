# Array, Matrix, Simulation
# Amazon 5 Opendoor 10 Bloomberg 5 Google 4 DoorDash 4 Dropbox 3 Adobe 3 Microsoft 2 Square 4 Snapchat 4
# Apple 4 Reddit 3 Facebook 3 Wish 3 Riot Games 2 Two Sigma
# https://leetcode.com/problems/game-of-life/

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and
# deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

from ast import List

# brute force: copy the board and update the original board based on rules

# use extra state: -1 for live_to_dead, 2 for dead_to_live
class GameofLife:
    NEIGHBORS = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
    LIVE_TO_DEAD = -1
    DEAD_TO_LIVE = 2
    LIVE = 1
    DEAD = 0

    def gameOfLife(self, board: List[List[int]]) -> None:
        row_count = len(board)
        col_count = len(board[0])
        for row in range(row_count):
            for col in range(col_count):
                self.update_board(board, row, col)

        # final update for intermediate states
        for row in range(row_count):
            for col in range(col_count):
                if board[row][col] == self.DEAD_TO_LIVE:
                    board[row][col] = self.LIVE
                elif board[row][col] == self.LIVE_TO_DEAD:
                    board[row][col] = self.DEAD

    def update_board(self, board, row, col):
        row_count = len(board)
        col_count = len(board[0])
        livecount = 0
        for row_delta, col_delta in self.NEIGHBORS:
            nr, nc = row + row_delta, col + col_delta
            if (
                0 <= nr < row_count
                and 0 <= nc < col_count
                and abs(board[nr][nc]) == self.LIVE
            ):
                # abs for live or live_to_dead
                livecount += 1
        if board[row][col] == self.LIVE:
            if livecount < 2 or livecount > 3:
                board[row][col] = self.LIVE_TO_DEAD
        if board[row][col] == self.DEAD:
            if livecount == 3:
                board[row][col] = self.DEAD_TO_LIVE

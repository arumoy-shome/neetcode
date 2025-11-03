"""Find the shortest path from top left to bottom right.
"""
class Solution:
    def shortestPath(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(ROWS), len(ROWS[0])
        visited = set()
        
        def dfs(row, col):
            if (row not in range(ROWS) or
                col not in range(COLS) or
                (row, col) in visited or
                grid[row][col] == 1
                ):
                return 0

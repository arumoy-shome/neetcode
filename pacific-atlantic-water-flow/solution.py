class Solution:
    def pacificAtlantic(self, grid: list[list[int]]) -> list[list[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        pac, atl = set(), set()

        def dfs(row, col, visited, prev_height):
            if (
                row not in range(ROWS)
                or col not in range(COLS)
                or (row, col) in visited
                or grid[row][col] < prev_height
            ):
                return

            visited.add((row, col))
            dfs(row + 1, col, visited, grid[row][col])
            dfs(row - 1, col, visited, grid[row][col])
            dfs(row, col + 1, visited, grid[row][col])
            dfs(row, col - 1, visited, grid[row][col])

        for c in range(COLS):
            dfs(0, c, pac, grid[0][c])
            dfs(ROWS - 1, c, atl, grid[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, grid[r][c])
            dfs(r, COLS - 1, atl, grid[r][COLS - 1])

        return [list(x) for x in pac & atl]


if __name__ == "__main__":
    # heights = [[4, 2, 7, 3, 4], [7, 4, 6, 4, 7], [6, 3, 5, 3, 6]]
    # heights = [[1], [1]]
    heights = [[2, 1], [1, 2]]
    print(Solution().pacificAtlantic(heights))

class Solution:
    def solve(self, grid: [list[list[str]]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col):
            if (
                row not in range(ROWS)
                or col not in range(COLS)
                or grid[row][col] != "O"
            ):
                return

            grid[row][col] = "T"
            print(f"found free land at {row, col}")
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for c in range(COLS):
            if grid[0][c] == "O":
                dfs(0, c)

            if grid[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c)

        for r in range(ROWS):
            if grid[r][0] == "O":
                dfs(r, 0)

            if grid[r][COLS - 1] == "O":
                dfs(r, COLS - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "O":
                    grid[r][c] = "X"

                if grid[r][c] == "T":
                    grid[r][c] = "O"


if __name__ == "__main__":
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "X", "O"],
    ]
    Solution().solve(board)
    print(board)

"""Count the number of unique paths from top left to bottom right."""


class Solution:
    def countPaths(self, grid: [list[list[int]]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        # count = 0

        def dfs(row, col):
            # nonlocal count
            if (
                row not in range(ROWS)
                or col not in range(COLS)
                or grid[row][col] == 1
                or (row, col) in visited
            ):
                return 0

            if row == ROWS - 1 and col == COLS - 1:
                return 1

            visited.add((row, col))
            count = 0
            count += dfs(row + 1, col)
            count += dfs(row - 1, col)
            count += dfs(row, col + 1)
            count += dfs(row, col - 1)
            visited.remove((row, col))
            
            return count

        return dfs(0, 0)


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0],
    ]
    print(Solution().countPaths(grid))

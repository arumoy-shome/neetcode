from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        islands = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(row, col):
            q = deque()
            q.append((row, col))

            while q:
                r, c = q.popleft()
                visited.add((r, c))

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if (
                        nr in range(ROWS)
                        and nc in range(COLS)
                        and grid[nr][nc] == "1"
                        and (nr, nc) not in visited
                    ):
                        q.append((nr, nc))

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1

        return islands


if __name__ == "__main__":
    grid = [
        ["0", "1", "1", "1", "0"],
        ["0", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print(Solution().numIslands(grid))

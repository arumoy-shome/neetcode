from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        if not grid:
            return

        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        DIRS = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row, col))
                    visited.add((row, col))

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if (
                        nr in range(ROWS)
                        and nc in range(COLS)
                        and (nr, nc) not in visited
                        and grid[nr][nc] == INF
                    ):
                        q.append((nr, nc))
                        visited.add((nr, nc))
            dist += 1


if __name__ == "__main__":
    grid = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647],
    ]
    Solution().islandsAndTreasure(grid)
    print(grid)

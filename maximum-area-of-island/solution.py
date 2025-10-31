from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0

        area = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(row, col):
            q = deque()
            q.append((row, col))

            res = 0
            while q:
                r, c = q.popleft()
                visited.add((r, c))
                res += 1

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if (
                        nr in range(ROWS)
                        and nc in range(COLS)
                        and (nr, nc) not in visited
                        and grid[nr][nc] == 1
                    ):
                        q.append((nr, nc))
            return res

        def dfs(row, col):
            if (
                row not in range(ROWS)
                or col not in range(COLS)
                or grid[row][col] == 0
                or (row, col) in visited
            ):
                return 0

            visited.add((row, col))

            return (
                1
                + dfs(row + 1, col)
                + dfs(row - 1, col)
                + dfs(row, col + 1)
                + dfs(row, col - 1)
            )

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = max(area, dfs(r, c))

        return area


if __name__ == "__main__":
    grid = [[0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 0, 0, 1]]
    print(Solution().maxAreaOfIsland(grid))

    grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    print(Solution().maxAreaOfIsland(grid))

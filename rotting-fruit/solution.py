from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        q = deque()
        time, fresh = 0, 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append((row, col))

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in DIRS:
                    nr, nc = dr + r, dc + c

                    if (
                        nr in range(ROWS)
                        and nc in range(COLS)
                        and grid[nr][nc] == 1
                    ):
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1


if __name__ == "__main__":
    grid = [[1, 1, 0], [0, 1, 1], [0, 1, 2]]
    print(Solution().orangesRotting(grid))

    grid = [[1, 0, 1], [0, 2, 0], [1, 0, 1]]
    print(Solution().orangesRotting(grid))

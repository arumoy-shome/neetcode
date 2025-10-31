import unittest
from collections import defaultdict


class Solution:
    """
    time complexity: O(9^2) because we have to iterate through each row and
    column
    space complexity: O(9^2) because we are storing 3 dicts, each storing up to
    9 groups which can contain upto 9 elements
    """

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue

                if (
                    val in rows[row]
                    or val in cols[col]
                    or val in squares[(row // 3, col // 3)]
                ):
                    return False

                rows[row].add(val)
                cols[col].add(val)
                squares[(row // 3, col // 3)].add(val)
        return True


class TestSolution(unittest.TestCase):
    def test_valid_board(self):
        board = [
            ["1", "2", ".", ".", "3", ".", ".", ".", "."],
            ["4", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", ".", "3"],
            ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
            [".", ".", ".", "8", ".", "3", ".", ".", "5"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", ".", ".", ".", ".", ".", "2", ".", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "8"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        self.assertTrue(Solution().isValidSudoku(board))

    def test_invalid_board(self):
        board = [
            ["1", "2", ".", ".", "3", ".", ".", ".", "."],
            ["4", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", "9", "1", ".", ".", ".", ".", ".", "3"],
            ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
            [".", ".", ".", "8", ".", "3", ".", ".", "5"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", ".", ".", ".", ".", ".", "2", ".", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "8"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        self.assertFalse(Solution().isValidSudoku(board))


if __name__ == "__main__":
    unittest.main()

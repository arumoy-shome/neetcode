import unittest


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            mid = top + ((bot - top) // 2)

            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break

        if top > bot:
            return False
        else:
            return self.search(matrix[mid], target)

    def search(self, nums: list[int], target) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return True

        return False


class TestSolution(unittest.TestCase):
    def test_1(self):
        matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
        target = 10
        self.assertTrue(Solution().searchMatrix(matrix, target))

    def test_2(self):
        matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
        target = 41
        self.assertFalse(Solution().searchMatrix(matrix, target))


if __name__ == "__main__":
    unittest.main()

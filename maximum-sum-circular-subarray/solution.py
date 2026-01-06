import unittest


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [-2, 4, -5, 4, -5, 9, 4]
        self.assertEqual(Solution().maxSubarraySumCircular(nums), 15)

    def test_2(self):
        nums = [2, 3, -4]
        self.assertEqual(Solution().maxSubarraySumCircular(nums), 5)

    def test_3(self):
        nums = [1, -2, 3, -2]
        self.assertEqual(Solution().maxSubarraySumCircular(nums), 3)


class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        glob_max, glob_min = nums[0], nums[0]
        cur_max, cur_min = 0, 0
        total = 0

        for num in nums:
            cur_max = max(cur_max + num, num)
            cur_min = min(cur_min + num, num)
            total += num
            glob_max = max(cur_max, glob_max)
            glob_min = min(cur_min, glob_min)

        return max(glob_max, total - glob_min) if glob_max > 0 else glob_max

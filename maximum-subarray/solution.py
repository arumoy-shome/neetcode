import unittest


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [2, -3, 4, -2, 2, 1, -1, 4]
        self.assertEqual(Solution().maxSubArray(nums), 8)

    def test_2(self):
        nums = [-1]
        self.assertEqual(Solution().maxSubArray(nums), -1)

    def test_3(self):
        nums = [-1, -4, -10]
        self.assertEqual(Solution().maxSubArray(nums), -1)


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0

        for num in nums:
            cur_sum = max(cur_sum + num, num)
            max_sum = max(max_sum, cur_sum)
        return max_sum

import unittest


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [2, 2, 2, 2, 5, 5, 5, 8]
        k = 3
        threshold = 4
        self.assertEqual(Solution().numOfSubarrays(nums, k, threshold), 3)


class Solution:
    def numOfSubarrays(self, nums: list[int], k: int, threshold: int) -> int:
        count = 0
        cur_sum = sum(nums[: k - 1])
        for left in range(len(nums) - k + 1):
            right = left + k - 1
            cur_sum += nums[right]

            if cur_sum / k >= threshold:
                count += 1

            cur_sum -= nums[left]
        return count

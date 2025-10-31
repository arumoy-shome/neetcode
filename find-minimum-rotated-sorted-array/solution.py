import unittest

class Solution:
    def findMin(self, nums: list[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            
            # in left sorted portion
            if nums[m] >= nums[l]:
                l = m + 1
            elif nums[m] <:
    
class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [3, 4, 5, 6, 1, 2]
        self.assertEqual(Solution().findMin(nums), 1)
    
if __name__ == "__main__":
    unittest.main()
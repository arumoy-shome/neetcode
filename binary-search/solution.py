import unittest


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m =  l + ((r - l) // 2)
            
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return m
                
        return -1


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums, target = [-1, 0, 2, 4, 6, 8], 4
        self.assertEqual(Solution().search(nums, target), 3)


if __name__ == "__main__":
    unittest.main()

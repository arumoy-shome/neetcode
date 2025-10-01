import unittest

class Solution:
    def remove(nums: list[int], val: int) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left

class TestSolution(unittest.TestCase):
    def test_remove_1(self):
        nums = [1, 1, 2, 3, 4]
        val = 1
        self.assertEqual(Solution.remove(nums, val), 3)

    def test_remove_2(self):
        nums = [0,1,2,2,3,0,4,2]
        val = 2
        self.assertEqual(Solution.remove(nums, val), 5)


if __name__ == "__main__":
    unittest.main()

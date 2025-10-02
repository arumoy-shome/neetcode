import unittest


class Solution:
    def pythonic(nums: list[int]) -> list:
        return nums + nums

    def concat(nums: list[int]) -> list:
        N = len(nums)
        # NOTE: can also initialize empty ans and use ans.insert(index, value)
        ans = [0] * N * 2

        for i in range(N):
            ans[i] = ans[i + N] = nums[i]

        return ans


class TestSolution(unittest.TestCase):
    # def test_pythonic(self):
    #     nums = [1,4,1,2]
    #     self.assertListEqual(Solution.pythonic(nums), [1,4,1,2,1,4,1,2])

    def test_concat(self):
        nums = [1, 4, 1, 2]
        self.assertListEqual(Solution.concat(nums), [1, 4, 1, 2, 1, 4, 1, 2])

    # def test_concat_2(self):
    #     nums = [22,21,20,1]
    #     self.assertListEqual(Solution.pythonic(nums), [22,21,20,1,22,21,20,1])


if __name__ == "__main__":
    unittest.main()

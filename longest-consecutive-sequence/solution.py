import unittest


class Solution:
    def longestConsecutive(self, nums: list[int]) -> list[int]:
        nums_set = set(nums)
        longest = 0

        for n in nums:
            # check if n is beginning of sequence
            if n - 1 not in nums_set:
                length = 0
                while n + length in nums_set:
                    length += 1
                longest = max(length, longest)
        return longest


class TestSolution(unittest.TestCase):
    def test_empty_nums(self):
        nums = []
        self.assertEqual(Solution().longestConsecutive(nums), 0)

    def test_nums_single_element(self):
        nums = [1]
        self.assertEqual(Solution().longestConsecutive(nums), 1)

    def test_nums_has_one_sequence(self):
        nums = [3, 1, 5]
        self.assertEqual(Solution().longestConsecutive(nums), 1)

    def test_nums_has_one_sequence_with_duplicates(self):
        nums = [3, 3, 5]
        self.assertEqual(Solution().longestConsecutive(nums), 1)

    def test_nums_has_multiple_sequences(self):
        nums = [1, 100, 4, 2, 3, 200]
        self.assertEqual(Solution().longestConsecutive(nums), 4)


if __name__ == "__main__":
    unittest.main()

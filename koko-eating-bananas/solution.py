import unittest
import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = l + ((r - l) // 2)
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)

            if hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        piles, h = [1, 4, 3, 2], 9
        self.assertEqual(Solution().minEatingSpeed(piles, h), 2)

    def test_2(self):
        piles, h = [25, 10, 23, 4], 4
        self.assertEqual(Solution().minEatingSpeed(piles, h), 25)


if __name__ == "__main__":
    unittest.main()

import unittest


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []  # tuples of index, temperature
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                iprev, _ = stack.pop()
                res[iprev] = i - iprev
            stack.append((i, t))
        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        temperatures = [22, 21, 20]
        self.assertListEqual(Solution().dailyTemperatures(temperatures), [0, 0, 0])

    def test_2(self):
        temperatures = [30, 38, 30, 36, 35, 40, 28]
        self.assertListEqual(
            Solution().dailyTemperatures(temperatures), [1, 4, 1, 2, 1, 0, 0]
        )


if __name__ == "__main__":
    unittest.main()

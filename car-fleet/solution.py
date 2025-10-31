import unittest


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(key=lambda x: x[0])
        stack = []

        for p, s in pairs[::-1]:
            stack.append((target - p) / s)  # append time to reach target
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


class TestSolution(unittest.TestCase):
    def test_1(self):
        target, position, speed = 10, [1, 4], [3, 2]
        self.assertEqual(Solution().carFleet(target, position, speed), 1)

    def test_2(self):
        target, position, speed = 10, [4, 1, 0, 7], [2, 2, 1, 1]
        self.assertEqual(Solution().carFleet(target, position, speed), 3)

    def test_3(self):
        target, position, speed = 10, [6, 8], [3, 2]
        self.assertEqual(Solution().carFleet(target, position, speed), 2)


if __name__ == "__main__":
    unittest.main()

import unittest


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            match token:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    r, l = stack.pop(), stack.pop()
                    stack.append(l - r)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    r, l = stack.pop(), stack.pop()
                    stack.append(int(l / r))
                case _:
                    stack.append(int(token))

        return stack.pop()


class TestSolution(unittest.TestCase):
    def test_1(self):
        tokens = ["1", "2", "+"]
        self.assertEqual(Solution().evalRPN(tokens), 3)

    def test_2(self):
        tokens = ["1", "2", "+", "3", "*"]
        self.assertEqual(Solution().evalRPN(tokens), 9)


if __name__ == "__main__":
    unittest.main()

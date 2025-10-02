import unittest


class Solution:
    def isvalid(s: str) -> bool:
        close_to_open = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []

        for char in s:
            if char in close_to_open:
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack


class TestSolution(unittest.TestCase):
    def test_isvalid(self):
        s = "()"
        self.assertTrue(Solution.isvalid(s))

    def test_isvalid_2(self):
        s = "([{}])"
        self.assertTrue(Solution.isvalid(s))

    def test_isvalid_3(self):
        s = "[(])"
        self.assertFalse(Solution.isvalid(s))


if __name__ == "__main__":
    unittest.main()

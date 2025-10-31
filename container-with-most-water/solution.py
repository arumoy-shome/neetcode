import unittest

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            w, h = r - l, min(heights[l], heights[r])
            area = w * h
            max_area = max(max_area, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -=1

        return max_area
    
class TestSolution(unittest.TestCase):
    def test_base_case_single_bar(self):
        heights = [1, 0]
        self.assertEqual(Solution().maxArea(heights), 0)
        
    def test_base_case(self):
        heights = [2, 4]
        self.assertEqual(Solution().maxArea(heights), 2)
        
    def test_equal_bars(self):
        heights = [2, 2, 2]
        self.assertEqual(Solution().maxArea(heights), 4)
        
    def test_multiple_bars(self):
        heights = [1,7,2,5,4,7,3,6]
        self.assertEqual(Solution().maxArea(heights), 36)
if __name__ == "__main__":
    unittest.main()
class Solution:
    def pythonic(nums: list[int]) -> int:
        return len(dict.fromkeys(nums))

    def pythonic2(nums: list[int]) -> int:
        return len(set(nums))

    def two_pointers(nums: list[int]) -> int:
        """
        Use this approach for O(1) space complexity.
        """
        left = 1
        for right in range(1, len(nums)):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left += 1

        return left

if __name__ == "__main__":
    assert Solution.pythonic([1, 2, 2, 3]) == 3
    assert Solution.pythonic2([1, 2, 2, 3]) == 3
    assert Solution.two_pointers([1, 2, 2, 3]) == 3

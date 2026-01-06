class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        nums_map = {}

        for i, n in enumerate(nums):
            if n in nums_map and i - nums_map[n] <= k:
                return True
            nums_map[n] = i

        return False

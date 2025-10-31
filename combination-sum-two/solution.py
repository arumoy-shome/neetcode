class Solution:
    def combinationSum2(self, nums: list[int], target: int) -> list[list[int]]:
        res = []
        nums.sort()

        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return
            if i == len(nums) or total > target:
                return

            # use nums[i]
            subset.append(nums[i])
            dfs(i + 1, subset, total + nums[i])

            # skip nums[i]
            subset.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, subset, total)

        dfs(0, [], 0)

        return res


if __name__ == "__main__":
    nums, target = [9, 2, 2, 4, 6, 1, 5], 8
    print(Solution().combinationSum2(nums, target))

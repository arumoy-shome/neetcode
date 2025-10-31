class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return
            if i == len(nums) or total > target:
                return

            subset.append(nums[i])
            dfs(i, subset, total + nums[i])

            subset.pop()
            dfs(i + 1, subset, total)

        dfs(0, [], 0)

        return res


if __name__ == "__main__":
    nums, target = [2, 5, 6, 9], 9
    print(Solution().combinationSum(nums, target))

    nums, target = [3, 4, 5], 16
    print(Solution().combinationSum(nums, target))

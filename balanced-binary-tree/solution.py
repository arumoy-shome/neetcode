class Solution:
    def isBalanced(self, node) -> bool:
        def dfs(node):
            if not node:
                return (True, 0)  # isbalanced, height

            left, right = dfs(node.left), dfs(node.right)

            isBalanced = abs(left[1] - right[1]) <= 1 and left[0] and right[0]
            return (isBalanced, 1 + max(left[1], right[1]))
        
        return dfs(node)[0]

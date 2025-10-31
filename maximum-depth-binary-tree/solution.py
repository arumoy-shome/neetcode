from collections import deque


class Solution:
    def maxDepth(self, root) -> int:
        """recursive DFS"""
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth(self, root) -> int:
        """BFS"""
        queue = deque()
        res = 0
        
        if root:
            queue.append(root)
            
        while queue:
            # process queue left to right
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res += 1
            
        return res

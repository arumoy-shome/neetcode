from collections import deque

class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        q = deque(root)
        res = []
        
        while q:
            vals = []
            for _ in range(len(q)):
                node = q.popleft()
                
                if node:
                    vals.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            res.append(vals)
            
        return res
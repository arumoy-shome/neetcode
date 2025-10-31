from collections import deque


class Solution:
    def rightSideView(self, root) -> list[int]:
        q = deque([root])
        res = []

        while q:
            rightmost = None
            for _ in range(len(q)):
                node = q.popleft()

                if node:
                    rightmost = node
                    q.append(node.left)
                    q.append(node.right)

            if rightmost:
                res.append(rightmost.val)

        return res

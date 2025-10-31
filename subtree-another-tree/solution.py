class Solution:
    def isSubtree(self, root, subroot) -> bool:
        def isSameTree(p, q) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        if not subroot:
            return True
        if not root:
            return False

        if isSameTree(root, subroot):
            return True

        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)


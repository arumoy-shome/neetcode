class Solution:
    def cloneGraph(self, node):
        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]

            copy = Node(val=node.val)
            old_to_new[node] = copy

            for n in node.neighbors:
                copy.neighbors.append(dfs(n))

            return copy

        return dfs(node) if node else None


if __name__ == "__main__":
    pass

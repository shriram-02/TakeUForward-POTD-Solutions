class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        clones = {}

        def dfs(node):
            if node in clones:
                return clones[node]

            clone = Node(node.val)
            clones[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)
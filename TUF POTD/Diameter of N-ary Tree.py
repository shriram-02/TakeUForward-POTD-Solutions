class Solution():
    def diameter(self, root):
        if not root:
            return 0

        self.ans = 0

        def dfs(node):
            if not node:
                return 0

            first = 0
            second = 0

            for child in node.children:
                h = dfs(child)

                if h > first:
                    second = first
                    first = h
                elif h > second:
                    second = h

            self.ans = max(self.ans, first + second)

            return first + 1

        dfs(root)
        return self.ans
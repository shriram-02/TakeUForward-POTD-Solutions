class Solution(object):
    def longestConsecutive(self, root):
        self.ans = 0

        def dfs(node):
            if not node:
                return 0, 0

            inc = dec = 1

            if node.left:
                left_inc, left_dec = dfs(node.left)

                if node.left.val == node.val + 1:
                    inc = max(inc, left_inc + 1)
                elif node.left.val == node.val - 1:
                    dec = max(dec, left_dec + 1)

            if node.right:
                right_inc, right_dec = dfs(node.right)

                if node.right.val == node.val + 1:
                    inc = max(inc, right_inc + 1)
                elif node.right.val == node.val - 1:
                    dec = max(dec, right_dec + 1)

            self.ans = max(self.ans, inc + dec - 1)

            return inc, dec

        dfs(root)
        return self.ans
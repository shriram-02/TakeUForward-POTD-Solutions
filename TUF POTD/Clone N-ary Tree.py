# Definition for an n-ary tree node.
# class TreeNode(object):
#     def __init__(self, val=0):
#         self.val = val
#         self.children = []

class Solution:
    def cloneTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        new_root = TreeNode(root.val)

        for child in root.children:
            new_root.children.append(self.cloneTree(child))

        return new_root
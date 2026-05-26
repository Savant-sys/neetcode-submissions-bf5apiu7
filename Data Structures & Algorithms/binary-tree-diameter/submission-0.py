# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #         1
        #       3   2
        #      3     4
        #     5       6
        #              7

        self.maxDiameter = 0

        def getHeight(node):
            if not node:
                return 0

            leftHeight = getHeight(node.left)
            rightHeight = getHeight(node.right)

            self.maxDiameter = max(self.maxDiameter, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)

        getHeight(root)
        return self.maxDiameter

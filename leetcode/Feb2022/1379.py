# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans=None
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.inorder(original,cloned,target)
        return self.ans

    def inorder(self, original: TreeNode, cloned: TreeNode, target: TreeNode):
        if original == target:
            self.ans= cloned
        if original.left:
            self.inorder(original.left,cloned.left,target)
        if original.right:
            self.inorder(original.right,cloned.right,target)
        return 
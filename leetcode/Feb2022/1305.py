# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.arr=[]
        self.inorder(root1)
        self.inorder(root2)
        self.arr.sort()
        return self.arr

    def inorder(self,root1):
        if root1 == None:
            return
        if root1.left:
            self.inorder(root1.left)
        self.arr.append(root1.val)
        if root1.right:
            self.inorder(self.right)
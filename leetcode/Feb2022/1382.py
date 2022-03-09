# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.arr=[]
        self.inorder(root)
        newRoot=None
        newRoot=self.helper(newRoot,self.arr)
        return newRoot

    def helper(self,root,nums):
        if len(nums) == 0:
            return
        mid=len(nums)//2
        root=TreeNode(nums[mid])
        root.left=self.helper(root,nums[:mid])
        root.right=self.helper(root,nums[mid+1:])
        return root
        
    def inorder(self,root):
        if root == None:
            return
        self.arr.append(root.val)
        if root.left:
            self.inorder(root.left)
        if root.right:
            self.inorder(root.right)
        return
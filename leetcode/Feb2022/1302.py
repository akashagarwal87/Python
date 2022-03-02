# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        maxDepth=0
        self.maxDepthG=0
        self.map={}
        maxDepth=self.indorder(root,maxDepth)
        return self.map[self.maxDepthG]

    def indorder(self,root,maxDepth):
        if root.left == None and root.right==None:
            if maxDepth in self.map:
                self.map[maxDepth]=self.map[maxDepth]+root.val
            else:
                self.map[maxDepth]=root.val
            self.maxDepthG=max(self.maxDepthG,maxDepth)
            return 
        maxDepth+=1
        if root.left:
            self.indorder(root.left,maxDepth)
        if root.right:
            self.indorder(root.right,maxDepth)
        return maxDepth
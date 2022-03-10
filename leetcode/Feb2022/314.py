# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result=[]
        if not root:
            return root
        self.result.append([root.val])
        if root.left:
            self.result.append([])
            self.preOrder(root.left,True,1,1)
        if root.right:
            self.result.append([])
            self.preOrder(root.left,False,2,2)

    def preOrder(self,root,isLeft,idx,variance):
        if not root:
            return
        if idx > 0 and idx >= len(self.result):
            self.result.append([])
        self.result[idx].append(root.val)
        if isLeft:
            if root.left:
                self.preOrder(root.left,True,idx+variance)
            if root.right:
                self.preOrder(root.right,True,idx-variance)
        else:
            if root.left:
                self.preOrder(root.left,False,idx-variance)
            if root.right:
                self.preOrder(root.right,False,idx+variance)
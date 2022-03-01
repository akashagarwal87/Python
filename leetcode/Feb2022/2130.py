# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head):
        n=0
        maxSum=0
        tmpHead=head
        while tmpHead:
            n+=1
            tmpHead=tmpHead.next
        i=0
        arr=[0]*(n//2)
        while head:
            if i <= (n//2)-1:
                arr[i]=head.val
            else:
                arr[n-1-i]+=head.val
            head=head.next
            i+=1
        return max(arr)
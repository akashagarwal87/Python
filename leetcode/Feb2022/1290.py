# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        arr=[0]
        result=0
        while head:
            arr.append(head.val)
            head=head.next
        n=len(arr)
        for i in range(n):
            result+=arr[i]**(n-i-2)
        return result

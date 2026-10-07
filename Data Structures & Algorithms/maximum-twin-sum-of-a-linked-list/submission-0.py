# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # edge case len = 2
        if (head.next.next == None):
            return head.val + head.next.val

        # find mid point
        i = head
        j = head
        while (j.next != None and j.next.next != None):
            i = i.next
            j = j.next.next
        mid = i

        # reverse second half
        prev = mid
        curr = mid.next
        while curr != None:
            save = curr.next
            curr.next = prev
            prev = curr
            curr = save
        
        # two point check
        i = head
        j = prev
        best = -1
        while (j != mid): #cond
            twinSum = i.val + j.val
            best = max(twinSum, best)
            
            i = i.next
            j = j.next
        return best





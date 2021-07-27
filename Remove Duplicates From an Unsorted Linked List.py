# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        myvar = head
        mydict = collections.defaultdict(int)

        while myvar:
            mydict[myvar.val] += 1
            myvar = myvar.next
        newvar = ListNode()
        newvar.next = head
        prev = newvar

        while head:
            if mydict[head.val] > 1:
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return newvar.next
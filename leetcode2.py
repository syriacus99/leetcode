# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy_l3 = ListNode()
        l3 = dummy_l3
        while l1 or l2 or carry:
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            carry,out = divmod(val1+val2+carry,10)
            l3.next = ListNode(out)
            l3 = l3.next
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        return dummy_l3.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev=head
        main=head.next
        head.next=None
        while main:
            temp=main.next
            main.next=prev
            prev=main
            main=temp

        return prev




        

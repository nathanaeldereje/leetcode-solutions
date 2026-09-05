# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        nums = {head.val}
        prev=head
        node=head.next
        while(node):
            if node.val in nums:
                prev.next=node.next
            else:
                nums.add(node.val)
                prev=node
            node=node.next
        return head



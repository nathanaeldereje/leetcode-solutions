# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return head

        temp= head
        prev = None
        node = head
        while(node):
            node_n = node.next
            if node_n and node.val == node_n.val:

                while node_n and node_n.val == node.val:
                    node_n = node_n.next
                if prev:
                    prev.next=node_n
                else:
                    head = node_n
                node=node_n
            else:
                prev=node
                node=node_n

        return head

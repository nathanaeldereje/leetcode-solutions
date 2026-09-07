# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev=None
        node=head
        n_1=None
        n_2=None
        count=0
        while(node):
            if count%2==0:
                n_1=node
                node=node.next
                
            else:
                if prev:
                    prev.next=node
                else:
                    head=node
                n_1.next=node.next
                node.next=n_1
                prev=n_1
                node=n_1.next
            count+=1
        return head

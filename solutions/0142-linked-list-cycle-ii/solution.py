# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        
        # Phase 1: Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:  # cycle detected
                break
        else:
            # No cycle found
            return None
        
        # Phase 2: Find the start of the cycle
        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        
        return slow  # This is the node where the cycle begins


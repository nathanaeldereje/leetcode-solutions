# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:  # type: ignore
            current = head
            count = 0
            while(current):
                count+=1
                current=current.next
            temp=head
        
            counter=count-n
            if count == 1:
                return None
            if counter == 0:
                return head.next
            index=0
            while(temp):
                index+=1
                if(index==counter):

                    next=temp.next
                    temp.next=next.next
                    # del current.next
                    break
                
                temp=temp.next
            return head

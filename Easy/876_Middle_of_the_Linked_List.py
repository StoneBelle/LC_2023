# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Determine length of linked list
        itr = head
        count = 0

        # Increase count while iterating through each element 
        while itr:
            count += 1 
            itr = itr.next
        
        # Find middle of LL 
        middle = count // 2
        itr = head # Reassign head 

        # Travere until middle of LL & return remaining untraversed part
        for m in range(middle):
            print(itr)
            itr = itr.next 
        return itr

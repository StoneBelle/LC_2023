# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # Retrieve data from LL & store in list
        data = []
    
        while head != None:
            data.append(head.val)
            head = head.next
        # reverse through all items in data & compare to OG data
        if data == data[::-1]:
            return True
        else:
            return False
        

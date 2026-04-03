# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head

        if head is None:
            return

        while temp != None:
            temp = temp.next
            length += 1
        
        removeIndex = length - n
        if removeIndex == 0:
            return head.next

        temp = head
        for i in range(length-1):
            if(i+1) == removeIndex:
                temp.next = temp.next.next
                break
            temp = temp.next
        return head
        # 0 - 0 - 0 - 0 - 0
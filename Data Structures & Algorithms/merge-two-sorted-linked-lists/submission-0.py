# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2

        if temp1 == None:
            return temp2
        elif temp2 == None:
            return temp1

        if temp1.val >= temp2.val:
            head_new = temp2
            temp2 = temp2.next
        else:
            head_new = temp1
            temp1 = temp1.next

        temp = head_new
        while temp1 != None or temp2 != None:
            if temp1 == None:
                temp.next = temp2
                temp2 = temp2.next
                temp = temp.next
                continue
            elif temp2 == None:
                temp.next = temp1
                temp1 = temp1.next
                temp = temp.next
                continue

            elif temp1.val >= temp2.val:
                temp.next = temp2
                temp2 = temp2.next
            else:
                temp.next = temp1
                temp1 = temp1.next
            temp = temp.next
        return head_new
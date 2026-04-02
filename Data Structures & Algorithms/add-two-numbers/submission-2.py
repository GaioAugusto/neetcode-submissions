# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        if temp1 == None:
            return temp2
        elif temp2 == None:
            return temp1

        result_list = ListNode(temp1.val + temp2.val)
        temp = result_list
        temp1 = temp1.next
        temp2 = temp2.next

        if temp.val > 9:
            carry_on = 1
            temp.val -= 10
        else:
            carry_on = 0
        
        if temp1 is None and temp2 is None and carry_on == 1:
            temp.next = ListNode(1)
            return result_list

        while temp1 or temp2:
            if temp1 == None: 
                # keep going with temp2
                temp.next = ListNode(temp2.val + carry_on)
                temp2 = temp2.next
            elif temp2 == None:
                # keep going with temp1
                temp.next = ListNode(temp1.val + carry_on)
                temp1 = temp1.next
            else:
                sum = temp1.val + temp2.val + carry_on
                temp.next = ListNode(sum)
                temp1 = temp1.next
                temp2 = temp2.next
            temp = temp.next
            if temp.val > 9:
                carry_on = 1
                temp.val -= 10
            else:
                carry_on = 0

            if temp1 is None and temp2 is None and carry_on == 1:
                temp.next = ListNode(1)
        
        return result_list

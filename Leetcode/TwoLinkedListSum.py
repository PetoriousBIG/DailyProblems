# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        listHead = ListNode(0) # dummy head
        thisNode = listHead    # we'll attach new nodes to list head using this variable 
        
        carry = 0 # for storing a tens digits if a sum is greater than 9
        list1Pointer = l1
        list2Pointer = l2
        
        while(list1Pointer is not None or list2Pointer is not None):
            # get next vals
            l1val = list1Pointer.val if list1Pointer is not None else 0
            l2val = list2Pointer.val if list2Pointer is not None else 0
            
            # calculate the sum and carry val
            sum = l1val + l2val + carry
            carry = sum / 10
            
            # attach value to list
            thisNode.next = ListNode(sum % 10)
            thisNode = thisNode.next
            
            # get next node, acts as looping variables 
            list1Pointer = list1Pointer.next if list1Pointer is not None else None
            list2Pointer = list2Pointer.next if list2Pointer is not None else None
            

        # in case a digit is left over
        if carry > 0:
            thisNode.next = ListNode(carry)
        
        return listHead.next
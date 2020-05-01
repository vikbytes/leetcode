#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
# For each integer pair: Add them together, if the result is > 9, carry over 1 to the next pair etc)

def addTwoNumbers(l1, l2):
    carry = False
    temp = 0
    result = []
    list1 = []
    list2 = []
    #Deconstruct the linked lists
    while(l1.next != None):
        list1.append(l1.val)
        l1.val = l1.next
    while(l2.next != None):
        list2.append(l2.val)
        l2.val = l2.next
    print(list1)
    print(list2)
    """
    while(True):
        temp = 0
        if carry == True:
            temp += 1
        temp += variable1 + variable2
        if temp > 9:
            carry = True
            temp = 9
        result.append(temp)
        if l1.next == None:
            break
        else:
            l1.val = l1.next
            l2.val = l2.next
    """

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def add_node(self,val):
        new_node = ListNode(val,self.next)
        self.next = new_node

def mergeTwoLists(l1,l2):
    result = ListNode()
    while(l1.val != None):
        result.val = l1.val
        result.add_node(l2)
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum1 = self.sumover(l1)
        sum2 = self.sumover(l2)
        outsum = list(str(sum1 + sum2))
        
        out = ListNode(None)
        orig = out
        for i in range(len(outsum)):
            out.next = ListNode(int(outsum.pop()))
            out = out.next
        return orig.next
    
    def sumover(self, l):
        s = 0
        d = 1
        while l:
            s += l.val * d
            l = l.next
            d = d * 10
        return s
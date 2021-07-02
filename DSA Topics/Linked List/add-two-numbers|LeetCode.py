# Problem Link
# https://leetcode.com/problems/add-two-numbers/submissions/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        v1:int = self.getValue(l1)
        v2:int = self.getValue(l2)
        ans = str(v1+v2)[::-1]
        root = ListNode(ans[0])
        prevNode = root
        for i in ans[1:]:
            newNode = ListNode(i)
            prevNode.next = newNode
            prevNode = newNode
        return root

    
    def getValue(self,node:ListNode):
        s = ''
        while node is not None:
            s+=str(node.val)
            node = node.next
        return int(s[::-1])
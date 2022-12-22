# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        stack = []
        while head is not None:
            stack.append(head.val)
            head=head.next

        node = None
        _head = ListNode(stack.pop())
        temp=_head
        while len(stack) > 0:
            temp.next=ListNode(stack.pop())
            temp=temp.next

        return _head







s=Solution()
l=ListNode(1,ListNode(2,ListNode(3,ListNode(4,None))))
s.reverseList(l)
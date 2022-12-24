# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        _head=head
        count=1
        while _head.next is not None:
            _head = _head.next
            count+=1


        if count % 2 == 0:
            count/=2
        else :
            count/=2

        _head=head
        i = 0
        for i in range(count):
            _head=_head.next
            i+=1

        return _head

s=Solution()
list=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6))))))
middleList=s.middleNode(list)









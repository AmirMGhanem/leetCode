# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x,next=None):
        self.val = x
        self.next = next

class Solution(object):
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow




s=Solution()

list=ListNode(3)
list.next=ListNode(2)
list.next.next=ListNode(0)
list.next.next.next=ListNode(-4)
list.next.next.next.next=list

node=s.detectCycle(list)
print(node.val)
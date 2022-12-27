
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """g
        :type root: Node
        :rtype: List[int]
        """
        result=[]
        if not root : return []
        s = [root]
        while len(s)>0:
            r = s.pop()
            result.append(r.val)
            s.extend(reversed(r.children))
        return result









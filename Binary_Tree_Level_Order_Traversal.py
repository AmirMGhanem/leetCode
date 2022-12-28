# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q= []
        lst= []
        if not root: return lst
        q.append(root)
        size=0
        while q :
            size=len(q)
            curval=[]
            while size>0:
                curr=q.pop(0)
                curval.append(curr.val)
                if curr.left : q.append(curr.left)
                if curr.right: q.append(curr.right)
                size-=1
            lst.append(curval)
        return lst





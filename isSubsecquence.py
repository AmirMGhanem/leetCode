class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for c in s:
            if t.find(c)>=0:
                temp=t.find(c)
                t=t[temp+1:]
            else:
                return False
        return True





s=Solution()
print(s.isSubsequence("abc","ahbgdc"))
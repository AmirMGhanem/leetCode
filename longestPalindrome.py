from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        _sum=0
        counter=Counter(s)
        odd=False
        print(counter)
        for c in counter.values():
            _sum+=c /2 *2
            if _sum%2==0 and c % 2 !=0:
                _sum+=1
        return _sum









s= Solution()
print(s.longestPalindrome("ccc"))
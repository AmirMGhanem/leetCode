class Solution(object):
    # credit to Timothy H Chang
    # source - https://www.youtube.com/watch?v=DVgseUp0qOY
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def helper(word):
            output,lookup=[],{}
            i=1
            for w in word:
                if w not in lookup:
                    lookup[w]=i
                    i+=1
                output.append(lookup[w])
            return output
        return helper(s)==helper(t)


s= Solution()
print(s.isIsomorphic("egg","add"))
class Solution(object):
    def fib(self,N):
        """
        :type n: int
        :rtype: int
        """
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            fibs = [0, 1]
            for number in range(N-1):
                fibs.append(fibs[-1] + fibs[-2])
            return fibs[-1]


s=Solution()
print(s.fib(9))


class Solution(object):
    # recursive solution
    def climbStairs(self,n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)



    # Iterative solution
    def climbStairsIterative(self,n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            a = 1
            b = 2
            for i in range(2,n):
                c = a + b
                a = b
                b = c
            return c


s=Solution()
print(s.climbStairs(5))
print(s.climbStairsIterative(5))


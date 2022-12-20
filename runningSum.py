class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum =0
        arr = []
        for n in nums:
            sum+=n
            arr.append(sum)
        return arr


s = Solution()
print(s.runningSum([1,2,3,4]))
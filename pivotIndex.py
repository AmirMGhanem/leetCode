class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: intw
        """
        if len(nums) == 1 :
            return 0
        for x in range(len(nums)):
            left = nums[0:x]
            right = nums[x+1:]
            sum_left=sum(left)
            sum_right=sum(right)
            if sum_right==sum_left:
                return x
        return -1

s = Solution()
print(s.pivotIndex([-1,-1,-1,-1,-1,0]))
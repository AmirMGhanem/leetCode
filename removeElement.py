class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = "_"

        while "_" in nums:
            nums.remove("_")
        return len(nums)


s=Solution()
nums=[3,2,2,3]
val=3
print(s.removeElement(nums,val))
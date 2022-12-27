class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        low = 0
        high = len(nums)
        mid=0

        while low <= high:
            mid=(low+high)/2
            if target>nums[mid]:
                low = mid+1

            elif target < nums[mid]:
                high = mid -1

            else : return mid

        return -1







s = Solution()
print(s.search([-1,0,3,5,9,12],12))








s= Solution()
s.search([-1,0,3,5,9,12],3)
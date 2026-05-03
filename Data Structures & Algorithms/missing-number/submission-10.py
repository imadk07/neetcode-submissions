class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if nums[0] == 1:
            return 0
       
        for i in range(1,len(nums)):
            if i != nums[i]:
                return i
        
        return nums[-1] +1


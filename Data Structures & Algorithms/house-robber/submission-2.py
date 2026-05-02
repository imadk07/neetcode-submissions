class Solution:
    def rob(self, nums: List[int]) -> int:
        n= len(nums)
        if not n :
            return 0
        if n <=2:
            return max(nums)

        rob1=nums[0]
        rob2=max(nums[0],nums[1])
        for i in range(2,n):
            
            curr = max((rob1+nums[i]),rob2)
            rob1=rob2
            rob2=curr
        return rob2


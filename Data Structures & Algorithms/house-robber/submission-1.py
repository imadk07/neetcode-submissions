class Solution:
    def rob(self, nums: List[int]) -> int:
        n= len(nums)
        if not n :
            return 0
        if n <=2:
            return max(nums)

        rob=[0]*(n)
        rob[0], rob[1]=nums[0],max(nums[0], nums[1])
        for i in range(2,n):
            rob[i] = max((rob[i-2]+nums[i]),rob[i-1])
        return rob[-1]


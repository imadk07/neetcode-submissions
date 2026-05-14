class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment not in seen:
                seen[nums[i]] = i
            else:
                return [seen[compliment],i]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, ond1 in enumerate(nums):
            ond2 = target - ond1            
            if ond2 in seen:
                return([seen[ond2],i])    
            seen[ond1] = i


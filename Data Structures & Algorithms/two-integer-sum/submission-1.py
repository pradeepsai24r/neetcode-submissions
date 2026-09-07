class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, op1 in enumerate(nums):
            op2 = target - op1
            if op2 in seen:
                return [seen[op2],i]
            seen[op1] = i
            
            
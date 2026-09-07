class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op=[]        
        for i in range(len(nums)):
            op.append(math.prod(nums[:i] + nums[i+1:]))
        return op

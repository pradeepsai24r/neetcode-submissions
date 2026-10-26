class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)-1
        while l <= r:
            i = (l+r)//2
            if nums[i] == target:
                return i
            elif target > nums[i]:
                l = i+1
            else:
                r = i-1
        return -1
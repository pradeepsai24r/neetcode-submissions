from typing import List
import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        m = []
        for i in range(n):
            m.append(math.prod(nums[:i] + nums[i+1:]))
            # print(nums[:i] + nums[i+1:])
        return m

s = Solution()
print(s.productExceptSelf([1,3,4,5]))
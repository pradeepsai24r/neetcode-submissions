# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         return len(set(nums)) != len(nums)
        
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = {}
        for i in nums:
            if i in temp:
                temp[i]+=1 
                return True
            else:
                temp[i]=1
        print(temp)
        return False
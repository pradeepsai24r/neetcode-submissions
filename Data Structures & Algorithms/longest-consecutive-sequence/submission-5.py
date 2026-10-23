class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        snums = sorted(set(nums))
        m_sq = sc = 1
        for i in range(1,len(snums)):
            if snums[i] == snums[i-1]+1:
                sc += 1
            else:
                sc = 1
            m_sq = max(m_sq, sc)
        return m_sq


    def longestConsecutive1(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # 1. Remove duplicates and sort
        s_nums = sorted(set(nums))

        # 2. check for longest seq         
        max_seq = 1
        seq_on = 1
        for i in range(0, len(s_nums)-1):
            if s_nums[i+1] == s_nums[i] + 1 :
                seq_on += 1
            else:
                max_seq = max(seq_on, max_seq)
                seq_on = 1
        return max(max_seq, seq_on)






# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         # 1. Remove duplicates and sort
#         s_nums = sorted(set(nums))
        
#         # 2. Iterate and count consecutive sequences
#         in_seq = 1
#         max_seq = 1
        
#         for i in range(1, len(s_nums)):
#             if s_nums[i] == s_nums[i - 1] + 1:
#                 in_seq += 1
#             else:
#                 max_seq = max(max_seq, in_seq)
#                 in_seq = 1
        
#         # Handle last sequence
#         max_seq = max(max_seq, in_seq)
        
#         return max_seq



        
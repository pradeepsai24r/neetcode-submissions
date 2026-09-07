class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # 1. Remove duplicates and sort
        s_nums = sorted(set(nums))
        
        # 2. Iterate and count consecutive sequences
        in_seq = 1
        max_seq = 1
        
        for i in range(1, len(s_nums)):
            if s_nums[i] == s_nums[i - 1] + 1:
                in_seq += 1
            else:
                max_seq = max(max_seq, in_seq)
                in_seq = 1
        
        # Handle last sequence
        max_seq = max(max_seq, in_seq)
        
        return max_seq



        
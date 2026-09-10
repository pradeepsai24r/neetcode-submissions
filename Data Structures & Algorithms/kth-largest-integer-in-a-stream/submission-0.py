class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.i_nums = nums
        self.i_k = k


    def add(self, val: int) -> int:
        self.i_nums.append(val)
        return self.k_large()
    
    def k_large(self) -> int:
        self.i_nums.sort(reverse=True)
        return(self.i_nums[self.i_k-1])


        

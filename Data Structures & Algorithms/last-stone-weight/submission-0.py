class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:  
        while len(stones) > 1:
            s_stones = sorted(stones)
            y, x = s_stones[-1], s_stones[-2]
            if x < y:
                stones.remove(y)
                stones.remove(x)
                stones.append(y - x)
            elif x == y:
                stones.remove(x)
                stones.remove(y)
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
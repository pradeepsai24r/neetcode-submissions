class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        max_area = 0
        while l < r:
            # calculate area
            a = (r-l) * min(heights[l], heights[r])
            # take max area w.r.t a
            max_area = max(max_area, a)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area 
            

    def maxAreaBF(self, heights: List[int]) -> int:
        res_area = 0
        for i in range(len(heights)):
            t_area = 0
            for j in range(i+1, len(heights)):
                area = min(heights[i], heights[j]) * (j - i)
                t_area = max(area, t_area)
            res_area = max(res_area, t_area)
        return res_area

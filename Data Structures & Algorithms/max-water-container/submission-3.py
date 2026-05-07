class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        start  end
        curr_max = min(start, end) * (end-start)
        increment lower pointer
        repeat
        '''
        l, r = 0, len(heights)-1
        output = 0

        while l<r:
            curr_max = min(heights[l],heights[r]) * (r-l)
            output = max(output, curr_max)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return output
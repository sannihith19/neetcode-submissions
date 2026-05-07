class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        
        38,1
        
        36,3
        
        40,5

        [1, 4, 1, 2, 1, 0, 0]
        '''
        output = [0 for _ in range(len(temperatures))]
        stack = []
        for curr_idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                output[stack[-1][1]] =  curr_idx - stack[-1][1]
                stack.pop()
            stack.append([temp, curr_idx])

        return output



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        2 20 4 10 3 4 5    
        '''
        temp = Counter(nums)
        max_count = 0
        for num in temp:
            count = 1
            while num - 1 in temp:
                count+=1
                num = num-1
            max_count = max(max_count, count)
        return max_count


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        1 2 4 6
        1 1 2 8
        48  24  6  1        
        '''
        length = len(nums)
        output = [1 for _ in range(length)]
        prefix = 1
        for i in range(length):
            output[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in reversed(range(length)):
            output[i] *= suffix
            suffix *= nums[i]
        return output 


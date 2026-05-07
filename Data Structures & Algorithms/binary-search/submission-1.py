class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
                middle = (left + right) // 2
                if nums[middle] == target:
                        return middle
                if target < nums[middle]:
                        right = middle-1
                else:
                        left = middle+1
        return -1



#-1 0 2 4 6 8






































        '''
       l, r = 0, len(nums)-1
        while l <= r:
            middle = (l+r) // 2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                l = middle + 1
            else:
                r = middle - 1
        return -1
            
            '''
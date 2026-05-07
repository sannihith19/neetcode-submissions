class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for idx, num in enumerate(nums):
            # if num = 
            l, r = idx+1, len(nums) - 1
            target = num
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            while l < r:
                curr_sum = nums[l] + nums[r] + target
                if curr_sum == 0:
                    output.append([nums[idx], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
                elif curr_sum < 0:
                    l+=1
                else:
                    r-=1
        return output
                    

                    


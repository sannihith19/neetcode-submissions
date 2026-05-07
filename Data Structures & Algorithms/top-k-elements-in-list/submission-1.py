class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        result = []
        mapping = [[] for _ in range(len(nums)+1)]
        
        for num, value in frequency.items():
            mapping[value].append(num)
        
        for num in mapping[::-1]:
            for i in num:
                result.append(i)
                if len(result) == k:
                    return result
            


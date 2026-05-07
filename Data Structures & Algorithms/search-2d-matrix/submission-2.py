class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix)-1

        while left<= right:
            middle = (left + right) // 2
            if matrix[middle][0] <= target <= matrix[middle][-1]:
                m = matrix[middle]
                l, r = 0, len(m)-1
                while l <= r:
                    c = (l+r)//2
                    if m[c] == target:
                        return True
                    if target<m[c]:
                        r = c-1
                    else:
                        l = c+1
                return False

            if target < matrix[middle][0]:
                right = middle-1
            else:
                left = middle+1
        return False
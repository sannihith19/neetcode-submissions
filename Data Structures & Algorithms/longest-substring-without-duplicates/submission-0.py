class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = output = 0
        seen = set()
        for r in s:
            while r in seen:
                seen.remove(s[l])
                l+=1
            seen.add(r)
            output = max(output, len(seen))
        return output
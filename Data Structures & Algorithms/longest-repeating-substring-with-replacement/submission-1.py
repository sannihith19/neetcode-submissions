class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counts = {}
        output = 0
        h_freq = 0
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r],0)
            h_freq = max(h_freq, counts[s[r]])

            if (r-l+1) - h_freq > k:
                counts[s[l]] -= 1
                l+=1
            output = max(output, r-l+1)

        

        return output





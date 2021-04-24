class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        counts = [0, 0]
        ans = 0
        
        for i in range(len(s)):
            c = int(s[i])
            # if current char is different from prev, reset count of curr char
            if i>0 and c!=int(s[i-1]):
                counts[c] = 0
            counts[c] += 1
            
            # if there is at least as many of the other char, then there must be a substring that has equal
            if counts[c]<=counts[1-c]:
                ans += 1
        
        return ans
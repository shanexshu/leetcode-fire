class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        n = len(p)
        p_letters = Counter(p)
        letters = Counter(s[0:n])
        if p_letters == letters:
            ans.append(0)
        for i in range(1, len(s)-n+1):
            letters[s[i-1]] -= 1
            letters[s[i-1+n]] += 1
            if p_letters == letters:
                ans.append(i)
                
        return ans
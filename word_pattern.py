class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = {}
        pat = {}
        ws = s.split()
        if len(pattern)!=len(ws): return False
        for i in range(len(pattern)):
            p = pattern[i]
            w = ws[i]
            if p in word and word[p]!=w: return False
            word[p] = w
            if w in pat and pat[w]!=p: return False
            pat[w] = p
        return True
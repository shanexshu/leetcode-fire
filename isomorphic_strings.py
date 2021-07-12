from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        dic = {}
        mapped = set()
        for i in range(len(s)):
            if s[i] not in dic:
                if t[i] in mapped: return False
                dic[s[i]] = t[i]
                mapped.add(t[i])
            else:
                if dic[s[i]] != t[i]:
                    return False
        return True
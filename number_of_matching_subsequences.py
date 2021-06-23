class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        ans = 0
        dic = {}
        for word in words:
            c0 = word[0]
            if c0 in dic:
                dic[c0].append(word)
            else:
                dic[c0] = [word]
        
        for c in s:
            if c in dic:
                found_words = dic[c]
                dic[c] = []                
                for word in found_words:
                    if len(word)==1: 
                        ans += 1
                    else:
                        c0 = word[1]
                        if c0 in dic:
                            dic[c0].append(word[1:])
                        else:
                            dic[c0] = [word[1:]]
        
        return ans
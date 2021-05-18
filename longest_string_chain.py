from collections import defaultdict
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        orgWords = defaultdict(list)
        n = len(words)
        maxlen = 0
        lens = []
        dp = defaultdict(int)

        for word in words:
            l = len(word)
            orgWords[l].append(word)
            maxlen = max(maxlen, l)
        
        
        ans = 0
        
        def isPred(pred, word):
            for i in range(len(word)):
                if pred==word[:i]+word[i+1:]:
                    return True
            return False
        
        for l in range(1, maxlen+1):
            for word in orgWords[l]:
                for word2 in orgWords[l-1]:
                    if isPred(word2, word):
                        dp[word] = max(dp[word], dp[word2]+1)
                        ans = max(ans, dp[word])
        
        return ans+1
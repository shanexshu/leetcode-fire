class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        def expand(i, j):
            while 0<=i<n and 0<=j<n and s[i]==s[j]:
                i-=1
                j+=1
            
            t = s[i+1:j]
            return len(t), t
        
        ans = ""
        for i in range(n):
            odd = expand(i,i)
            even = expand(i, i+1)
            
            if odd[0]>len(ans):
                ans = odd[1]
            if even[0]>len(ans):
                ans = even[1]
        
        return ans
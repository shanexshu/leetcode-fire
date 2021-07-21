class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        '''
        create a cumulative shifts array by going backwards
        loop through s and shift each
        Time: O(n)
        Space O(n)
        '''
        
        cum_shifts = [shifts[-1]]*len(shifts)
        for i in reversed(range(len(shifts)-1)):
            cum_shifts[i] = cum_shifts[i+1] + shifts[i]
        
        ans = []
        for i in range(len(s)):
            c = ord(s[i])-ord('a')   # range: 0-25
            c = (c+cum_shifts[i])%26

            ans.append(chr(c+ord('a')))
        
        return "".join(ans)
        
        
        
        
'''
3,5,9
17,14,9
abc
3
55
999


shifts = 3,5,9
cum_shifts = 17,14,9
s = abc
      i
ans = rpl
'''
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        seq = '123456789'

        for length in range(len(str(low)), len(str(high))+1):
            for start in range(10 - length):
                num = int(seq[start:start+length])
                if low <= num <= high:
                    ans.append(num)
        
        return ans
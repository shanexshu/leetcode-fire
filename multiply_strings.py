class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        k1 = 1
        k2 = 1
        
        for i in range(len(num2)-1,-1,-1):
            n2 = ord(num2[i])-ord('0')
            k2 = 1
            for j in range(len(num1)-1,-1,-1):
                n1 = ord(num1[j])-ord('0')
                ans += n1*n2*k1*k2
                k2 *= 10
            k1 *= 10
        
        return str(ans)
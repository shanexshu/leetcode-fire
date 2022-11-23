class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = n
        while num > 1:
            if num in seen: return False
            seen.add(num)
            
            squaredSum = 0
            digits = num
            while digits > 0:
                digit = digits % 10
                squaredSum += digit*digit
                digits //= 10
            num = squaredSum
            
        return True
        
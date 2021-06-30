from collections import deque
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0]*n
        used = deque()
        ans = 0
        cur = 0
        
        for i in range(n):
            if nums[i] == 1:
                cur += 1
            else:
                
                if len(used)<k:
                    cur += 1
                    used.append(i)
                else:
                    cur = 0
                    if used:
                        lr = used.popleft()
                        cur = i-lr
                        used.append(i)

            ans = max(ans, cur)
            
        return ans
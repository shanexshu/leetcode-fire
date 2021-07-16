from collections import Counter
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        counts = Counter(nums)
        ans = []
        curState = []
        
        def backtrack(i):
            if i>=len(nums): return
            if len(curState)==3:
                # look for last number in counts
                x = target-sum(curState)
                if x < nums[i]: 
                    # case where the 2nd value no longer valid (done)
                    return 1
                if x in counts and counts[x]>0:
                    if (curState + [x]) not in ans:
                        ans.append(curState + [x])
                return
            for j in range(i, len(nums)-1):
                curState.append(nums[j])
                counts[nums[j]] -= 1
                done = backtrack(j+1)
                curState.pop()
                counts[nums[j]] += 1
                if done: 
                    break

        backtrack(0)
        return ans

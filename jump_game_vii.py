class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        reachable = [c=='0' for c in s]
        prev_reach = 0    # num of indices where you could have jumped from
        
        for i in range(1, n):
            if i-minJump>=0:
                # right side of sliding window; potentially gain ability to jump from somewhere
                prev_reach += reachable[i-minJump]
            if i-maxJump-1>=0:
                # left side of sliding window; potentially lose a jumping origin as it falls out of window
                prev_reach -= reachable[i-maxJump-1]
            
            reachable[i] &= (prev_reach > 0)
            
        return reachable[-1]
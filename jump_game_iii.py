class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [0]*len(arr)
        q = deque([start])
        while q:
            i = q.popleft()
            if arr[i]==0: return True
            for sign in (-1,1):
                next_i = i + sign * arr[i]
                if 0 <= next_i < len(arr) and visited[next_i] == 0:
                    q.append(next_i)
                    visited[next_i] = 1
                    
        return False
        
        
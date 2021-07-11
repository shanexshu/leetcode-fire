class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        
        # intuition: because tree, there are no cycles, so only one path to target
        # 
        # bfs from starting position
        # pass along 1/(num of neighbors) and 1 second increment on time
        # when target is found, return product of all probs, unless time>t
        
        adj = [set() for _ in range(n+1)]
        neighbors = [0]*(n+1)
        for a,b in edges:
            adj[a].add(b)
            adj[b].add(a)
            neighbors[a] += 1
            neighbors[b] += 1
        visited = set()
        
        # queue will hold (vertex, cum prob, time)
        q = deque([(1, 1, 0)])
        while q:
            v, prob, time = q.popleft()
            visited.add(v)
            if v == target:
                if time > t:
                    return 0
                if time < t:
                    if neighbors[v]>0: return 0
                return prob
                
            num_nei = neighbors[v]
            for nei in adj[v]:
                neighbors[nei] -= 1    # each next vertex will not be able to go back to v
                if nei not in visited:
                    q.append((nei, prob*1/num_nei, time+1))
        
        return 0
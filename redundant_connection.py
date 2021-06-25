class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        neighbors = [set() for _ in range(n+1)]
        
        def dfs(u, v):
            # return True if you can find v starting from u
            if u == v: return True
            for nei in neighbors[u]:
                if nei not in seen:
                    seen.add(nei)
                    if dfs(nei, v): return True
            return False
            
        
        for u,v in edges:
            if (neighbors[u] and neighbors[v]):
                seen = set()
                if dfs(u, v): return [u, v]
            neighbors[u].add(v)
            neighbors[v].add(u)
                
        return [0, 0]
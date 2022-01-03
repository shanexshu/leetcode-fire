class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        trust_tofrom = {}
        for i in range(len(trust)):
            from_, to_ = trust[i]
            
            if to_ not in trust_tofrom:
                trust_tofrom[to_] = [0,1]
            else:
                trust_tofrom[to_][1] += 1
            
            if from_ not in trust_tofrom:
                trust_tofrom[from_] = [1,0]
            else:
                trust_tofrom[from_][0] += 1
        
        for n_ in range(1, N+1):
            if n_ in trust_tofrom:
                if trust_tofrom[n_][0]==0 and trust_tofrom[n_][1]==N-1:
                    return n_
            else:
                if N==1:
                    return 1
        return -1
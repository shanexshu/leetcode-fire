class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        self.seq = [0]*(2*n-1)
        def backtrack(i):
            if i==(2*n-1):
                return 1
            if self.seq[i] > 0:
                return backtrack(i+1)
            for j in range(n,0,-1):
                if j not in self.seq:
                    if j==1:
                        if self.seq[i] > 0: return
                        self.seq[i] = j
                    else:
                        if i+j>=len(self.seq): continue
                        if self.seq[i] + self.seq[i+j] > 0: continue
                        self.seq[i] = j
                        self.seq[i+j] = j
                    if backtrack(i+1):
                        return 1
                    self.seq[i] = 0
                    if j>1:
                        self.seq[i+j] = 0
            
            return 0
        
        backtrack(0)
        return self.seq
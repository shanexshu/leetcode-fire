import math
class MinStack:
    
    def __init__(self):
        # stack will hold val, min
        self.stack = []
        self.mins = []
        
    def push(self, val):
        newMin = val
        if self.mins:
            newMin = min(newMin, self.mins[-1])
        self.stack.append(val)
        self.mins.append(newMin)
    
    def pop(self):
        self.stack.pop()
        self.mins.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.mins[-1]
        
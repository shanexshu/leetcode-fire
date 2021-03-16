class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = [0,0]
        
        global facing
        facing = 0 # NESW = 0123
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        
        def move(ins):
            global facing
            if ins == 'G':
                pos[0] += dirs[facing][0]
                pos[1] += dirs[facing][1]
            if ins == 'L':
                facing = (facing-1)%4
            if ins == 'R':
                facing = (facing+1)%4
        
        for _ in range(4):
            for i in instructions:
                move(i)
            if pos == [0,0]: return True
                
        return False
class Solution:
    def calculate(self, s: str) -> int:
        ans = []
        parsed = []
        currNum = []
        for char in s:
            if char.isdigit():
                currNum.append(char)
            elif char!=' ':
                parsed.append(int("".join(currNum)))
                parsed.append(char)
                currNum = []
        parsed.append(int("".join(currNum)))
        
        working = []
        i = 0
        while i < len(parsed):
            if parsed[i]=="*":
                working[-1] *= parsed[i+1]
                i += 2
            elif parsed[i]=="/":
                div = working[-1]/parsed[i+1]
                if div < 0:
                    working[-1] = int(math.ceil(div))
                else:
                    working[-1] = int(math.floor(div))
                i += 2
            else:
                working.append(parsed[i])
                i += 1
        i = 0
        parsed = working[:]
        working = []
        while i < len(parsed):
            if parsed[i]=="+":
                working[-1] += parsed[i+1]
                i += 2
            elif parsed[i]=="-":
                working[-1] -= parsed[i+1]
                i += 2
            else:
                working.append(parsed[i])
                i += 1
        return working[0]
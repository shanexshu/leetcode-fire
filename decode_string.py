class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []

        for char in s:
            if char!="]":
                stack.append(char)
            else:
                currStr = []
                num = []
                while stack and stack[-1].isalpha():
                    letter = stack.pop()
                    currStr = [letter] + currStr
                stack.pop()
                while stack and stack[-1].isdigit():
                    digit = stack.pop()
                    num = [digit] + num
                stack.append(int("".join(num)) * "".join(currStr))
            
        return "".join(stack)

'''
"abc3[cd]xyz"
           i

stack = a,b,c,cdcdcd,x,y,z

currStr = cd
num = 3





"3[a2[c]]"
       i

stack = 3,[,a,cc

currStr = c
num = 2

num*currStr

"2[abc]3[cd]ef"
              i

stack = 

ans = abcabccdcdcdef

currStr = 
num = 



'''

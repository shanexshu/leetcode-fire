class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
    	# ()())()
        #       c
        # open: 0
        # errors: 1
        # (()))
        #     c
        # (()(())))()((
        #             c 
        # loop through string, keep track of open paren
        # decrement open when seeing ‘)’
        # if count would go negative, increment errors
        # at the end, add to errors the number of open

        op = 0
        errors = 0
        ans = []
        for c in s:
            if c=='(':
                op += 1
            elif c==')':
                op -= 1
            if op<0:
                errors += 1
                op = 0
            else:
                ans.append(c)

        # go back and replace error ) with blanks
        i = len(ans)-1
        while op>0:
            if ans[i]=='(':
                ans[i] = ''
                op -= 1
            i -= 1
        return ''.join(ans)

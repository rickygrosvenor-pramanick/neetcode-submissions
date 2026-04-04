class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open_brackets = 0
        close_brackets = 0

        stack = []
        ret = []

        def backtrack(open_num, close_num):
            if open_num == close_num  == n:
                ret.append("".join(stack))
                return
            if open_num < n:
                stack.append("(")
                backtrack(open_num + 1, close_num)
                # we have single stack so pop the char we pushed earlier i.e. "("
                # we are not passing the stack into recursion, its our global variable
                stack.pop()
            if close_num < open_num:
                # takes care of adding only "(" when open_num == close_num < n
                stack.append(")")
                backtrack(open_num, close_num + 1)
                stack.pop()
        
        backtrack(0, 0)
        return ret
        
        
class MinStack:

    def __init__(self):
        self.stack = []
        # The key logic lies in keeping the min_stack perfectly 
        # synchronized with the main stack. Every time you perform 
        # an operation on the main stack, you perform a corresponding 
        # operation on the min_stack.
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        popped = self.stack.pop()
        # we pop the min_stack as we are getting rid of the min
        # for the popped element
        self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        

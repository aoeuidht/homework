class MinStack:
    def __init__(self):
        self.stack = []
        self.m = None
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        self.m = x if (self.m is None) else min(self.m, x)
        return x

    # @return nothing
    def pop(self):
        if not self.stack:
            return
        r = self.stack.pop()
        if r == self.m:
            self.m = min(self.stack) if self.stack else None

    # @return an integer
    def top(self):
        return self.stack[-1] if self.stack else None

    # @return an integer
    def getMin(self):
        return self.m

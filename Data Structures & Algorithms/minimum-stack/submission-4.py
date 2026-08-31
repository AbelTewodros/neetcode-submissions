class MinStack:

    def __init__(self):
        self.stack = []
        self.min_tracker = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_tracker and self.min_tracker[-1] < val:
            self.min_tracker.append(self.min_tracker[-1])
        else:
            self.min_tracker.append(val)
            

    def pop(self) -> None:
        self.stack.pop()
        self.min_tracker.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_tracker[-1]

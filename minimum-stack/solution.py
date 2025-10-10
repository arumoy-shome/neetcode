class MinStack:
    def __init__(self):
        self.min = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min.append(min(val, self.min[-1] if self.min else val))

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

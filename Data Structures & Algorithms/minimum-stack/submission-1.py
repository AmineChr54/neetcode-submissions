class MinStack:

    def __init__(self):
        self.items = []

    def push(self, val: int) -> None:
        if not self.items:
            # If the stack is empty, this first value is automatically the minimum
            self.items.append((val, val))
        else:
            # Compare current value with the minimum of the element below it
            current_min = self.items[-1][1]
            self.items.append((val, min(val, current_min)))
        
    def pop(self) -> None:
        if self.items:
            self.items.pop()


    def top(self) -> int:
        if self.items:
            return self.items[-1][0]  # Return the actual value
        return None

    def getMin(self) -> int:
        if self.items:
            return self.items[-1][1]  # Return the actual value
        return None
        

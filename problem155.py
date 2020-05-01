class MinStack:
    def __init__(self):
        self.val = []
    
    def push(self, x):
        self.val.append(x)
    
    def pop(self):
        self.val.pop()

    def top(self):
        return self.val[-1]
    
    def getMin(self):
        temp = 0
        for x in self.val:
            if x < temp:
                temp = x
        return temp

minStack = MinStack()

minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())
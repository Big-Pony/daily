class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize=maxSize
        self.stack=[]

    def push(self, x: int) -> None:
        if len(self.stack)<self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack)>=1:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        n=k
        if k>len(self.stack):
            n=len(self.stack)
        for i in range(n):
            self.stack[i]+=val
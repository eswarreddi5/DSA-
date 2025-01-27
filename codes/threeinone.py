class multistack:
    def __init__(self,satcksize):
        self.numstack = 3
        self.array = [0]*(self.numstack*satcksize)
        self.sizes = [0]*self.numstack
        self.stacksize = satcksize
    def isempty(self,stacknum):
        if self.sizes[stacknum]==0:
            return True
        return False
    def isfull(self,stacknum):
        if self.sizes[stacknum]==self.stacksize:
            return True
        return False
    def indexoftop(self,stacknum):
        if self.isempty(stacknum):
            return "stack is empty"
        else:
            offset = stacknum*self.stacksize
            return offset + self.sizes[stacknum]-1
    def push(self,satcknum,item):
        if self.isfull(satcknum):
            return "Stack is full"
        else:
            self.sizes[satcknum]+=1
            self.array[self.indexoftop(satcknum)] = item
    def pop(self,stacknum):
        if self.isempty(stacknum):
            return "satck is empty"
        value = self.array[self.indexoftop(stacknum)]
        self.array[self.indexoftop(stacknum)]=0
        self.sizes[stacknum]-=1
        return value
    def peek(self,stacknum):
        if self.isempty(stacknum):
            return "stack is empty"
        return self.array[self.indexoftop(stacknum)]
mystack = multistack(4)
mystack.push(0,1)
mystack.push(0,1)
mystack.push(1,2)
mystack.push(2,3)
print(mystack.array)



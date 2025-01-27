class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len  = 0
    def add_begin(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            n = Node(data)
            n.next = self.head
            self.head = n
        self.len+=1
    def traverse_ele(self):
        if self.head is None:
            print("List is None")
        else:
            n = self.head
            while n:
                print(n.data,end="-->")
                n = n.next
    def add_toend(self,data):
        if self.head is None:
            self.head =Node(data)
            self.tail = self.head
        else:
            new = Node(data)
            self.tail.next = new
            self.tail  = new
        self.len+=1
    def add_middle(self,data):
        n = self.head
        newnnode = Node(data)
        for x in range(int(self.len/2)):
            n = n.next
        newnnode.next = n.next
        n.next = newnnode
        self.len+=1
    def search(self,ele):
        if self.head is None:
            print("list is empty.")
        else:
            n = self.head
            while n.next:
                if n.data == ele:
                    print("data found in the linked list")
                    break
                n = n.next
            else:
                print("no data found")
    def get(self,index):
        if index==-1:
            print(f"index value found {self.tail}")
        if index<-1 or index>self.len:
            print("Index out of range...")
        else:
            n = self.head
            for _ in range(index-1):
                n = n.next
        return n
    def set(self,index,dat):
        temp  = self.get(index)
        if temp :
            temp.data = dat
            return True
        return False
    def pop_fisrt(self):
        if self.head is None:
            print("List is empty.")
        else:
            popnode = self.head
            self.head = self.head.next
            popnode.next = None
            self.len-=1
            return f"{popnode.data} has been popped"
    def pop(self):
        if self.head is None:
            return None
        popnode = self.tail
        if self.len==1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.len-=1
        return f"{popnode.data} has been popped"
    def remove(self,index):
        prev_node = self.get(index-1)
        popednode = prev_node.next
        prev_node.next = popednode.next
        popednode.next = None
        self.len-=1
        return f"{popednode.data} has been popped"
    def remove_all(self):
        self.head = None
        self.tail = None
        self.len = 0
    def reverse(self):
        prev = None
        cur  = self.head
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        self.head,self.tail = self.tail,self.head
    def nthlast(self,n):
        if self.head is None:
            return None
        else:
            temp = self.head
            for x in range(self.len-n):
                temp = temp.next
        return temp.data
    def partition(self,x):
        curnode = self.head
        self.tail = self.head
        while curnode:
            nextnode = curnode.next
            curnode.next = None
            if curnode.data<x:
                curnode.next = self.head
                self.head = curnode
            else:
                self.tail.next = curnode
                self.tail = curnode
            curnode = nextnode
        if self.tail.next is  not None:
            self.tail.next = None

    @classmethod
    def sumlinekd(cls,ll1,ll2):
        n1 = ll1.head
        n2 = ll2.head
        ll3 = LinkedList()
        carry = 0
        while n1 or n2 :
            result = carry
            if n1:
                result+=n1.data
                n1 = n1.next
            if n2:
                result+=n2.data
                n2 = n2.next
            ll3.add_begin(result%10)
            carry = result//10
        return ll3.traverse_ele()
    @classmethod
    def addsamenode(cls,ll1,ll2,value):
        temp = Node(value)
        ll1.tail.next = temp
        ll1.tail  = temp
        ll2.tail.next = temp
        ll2.tail  = temp
    def intersection(cls,ll1,ll2):
        if ll1.tail is not ll2.tail:
            return False
        lena = ll1.len
        lenb = ll2.len
        short = ll1 if lena<lenb else ll2
        long  = ll2 if lena<lenb else ll1
        dif = long.len - short.len
        long = long.head
        short = short.head
        for i in range(dif):
            long = long.next
        while short is not long:
            short = short.next
            long = long.next
        return long.data
    
    

ll = LinkedList()
ll1 = LinkedList()
ll1.add_toend(7)
ll1.add_toend(1)
ll1.add_toend(6)
ll2 = LinkedList()
ll2.add_toend(5)
ll2.add_toend(9)
ll2.add_toend(2)

ll.addsamenode(ll1,ll2,11)
print(ll.intersection(ll1,ll2))
ll2.traverse_ele()
print()
ll1.traverse_ele()
'''
ll.add_begin(4)
ll.add_begin(5)
ll.add_begin(6)
ll.add_begin(7)
ll.add_toend(3)
ll.add_middle(0)
print(ll.len)
ll.traverse_ele()
print()
print(ll.nthlast(3))
ll.partition(5)
ll.traverse_ele()
ll.traverse_ele()
print()
ll.search(6)
ll.get(2)
ll.set(1,9)
ll.traverse_ele()
print()
print(ll.pop_fisrt())
print(ll.pop())
print(ll.remove(3))
ll.traverse_ele()
ll.reverse()
print()
ll.traverse_ele()'''
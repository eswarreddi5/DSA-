class graph:
    def __init__(self):
        self.adjacency_list = {}
    def add_vertex(self,vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,":",self.adjacency_list[vertex])
    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    def remove_edge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].remove(vertex2)
            self.adjacency_list[vertex2].remove(vertex1)
            return True
        return False
    def remove_vertex(self,vertex1):
        if vertex1 in self.adjacency_list.keys():
            for x in self.adjacency_list[vertex1]:
                self.adjacency_list[x].remove(vertex1)
            del self.adjacency_list[vertex1]
            return True
        return False
    def bfs(self,vertex):
        visited = set()
        visited.add(vertex)
        queue = [vertex]
        while len(queue)>0:
            current  = queue.pop(0)
            print(current,end=" ")
            for i in self.adjacency_list[current]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
    def dfs(self,vertex):
        visited =set()
        stack =[vertex]
        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                print(current_vertex,end=" ")
                visited.add(current_vertex)
            for i in self.adjacency_list[current_vertex]:
                if i not in visited:
                    stack.append(i) 
    def dfsi(self,vertex):
        visited = set()
        stack =[]
        stack = [vertex]
        while stack:
            cur = stack.pop()
            if cur not in visited:
                visited.add(cur)
                print(cur,end=" ")
            for i in self.adjacency_list[cur]:
                if i not in visited:
                    stack.append(i)
                     
Graph = graph()
Graph.add_vertex("A")
Graph.add_vertex("B")
Graph.add_vertex("C")
Graph.add_vertex("D")
Graph.add_vertex("E")
Graph.add_edge("A","B")
Graph.add_edge("A","C")
Graph.add_edge("A","D")
Graph.add_edge("D","E")
Graph.add_edge("B","C")
Graph.add_edge("C","D")

Graph.dfs("A")


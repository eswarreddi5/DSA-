def kruskal(edges):
    mst = [[] for _ in range(len(edges))]
    edgelist = []
    for source,vertex in enumerate(edges):
        for edge in vertex:
            if edge[0]>source:
                edgelist.append([source,edge[0],edge[1]])
    sortededges = sorted(edgelist,key=lambda edge:edge[2])
    parents = [i for i in range(len(edges))]
    rank = [0 for j in range(len(edges))]
    for edge in sortededges:
        xroot = find(edge[0],parents)
        yroot = find(edge[1],parents)
        if xroot!=yroot:
            mst[edge[0]].append([edge[1],edge[2]])
            mst[edge[1]].append([edge[0],edge[2]])
            union(xroot,yroot,rank,parents)
    return mst
def find(edge,parents):
    if edge!=parents[edge]:
        parents[edge]  = find(parents[edge],parents)
    return parents[edge]
def union(xroot,yroot,rank,parents):
    if rank[xroot]<rank[yroot]:
        parents[xroot] = yroot
    elif rank[xroot]>rank[yroot]:
        parents[yroot] = xroot
    else:
        parents[yroot] = xroot
        rank[xroot]+=1
edges = [[[1,3],[2,5]],
         [[0,3],[2,10],[3,12]],
         [[0,5],[1,10]],
         [[1,12]]]
print(kruskal(edges))
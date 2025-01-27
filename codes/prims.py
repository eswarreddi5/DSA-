import heapq
def prims(edges):
    mst = [[] for _ in edges]
    visited = set([0])
    minheap = [(weight,0,destination) for destination,weight in edges[0]]
    heapq.heapify(minheap)
    for _ in range(len(edges)-1):
        nextweight,nextorigin,nextdestination = heapq.heappop(minheap)
        while nextdestination in visited and minheap:
            nextweight,nextorigin,nextdestination = heapq.heappop(minheap)
        visited.add(nextdestination)
        mst[nextorigin].append([nextdestination,nextweight])
        mst[nextdestination].append([nextorigin,nextweight])
        for nodeidx,weight in edges[nextdestination]:
            if nodeidx in visited:continue
            heapq.heappush(minheap,(weight,nextdestination,nodeidx))
    return mst
edges = [[[1,3],[2,5]],
         [[0,3],[2,10],[3,12]],
         [[0,5],[1,10]],
         [[1,12]]]
print(prims(edges))


def primsalgo(edges):
    visited = [0 for _ in range(len(edges))]
    nodes = [i for i in range(len(edges))]
    visited[0] = True
    mst = []
    edgenum = 0
    while edgenum<len(edges)-1:
        min = float("iNF")

        for i in range(len(edges)):
            if visited[i]:
                for j in range(len(edges)):
                    if (not visited[j] and edges[i][j]):
                        if min>edges[i][j]:
                            min = edges[i][j]
                            s = i
                            d = j
        mst.append([nodes[s],nodes[d],edges[s][d]])
        visited[d] = True
        edgenum+=1
    return mst
edges = [[0,10,20,0,0],
         [10,0,30,5,0],
         [20,30,0,15,6],
         [0,5,15,0,8],
         [0,0,6,8,0]]
print(primsalgo(edges))

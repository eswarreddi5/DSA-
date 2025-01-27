from collections import defaultdict
def topological(dependecies,jobs):
    graph = defaultdict(list)
    indegree = {job:0 for job in jobs}
    for u,v in dependecies:
        graph[u].append(v)
        indegree[v]+=1
    queue = [i for i in jobs if indegree[i]==0]
    res = []
    while queue:
        out = queue.pop(0)
        res.append(out)
        for i in graph[out]:
            indegree[i]-=1
            if indegree[i]==0:
                queue.append(i)
    if len(res)!=len(jobs):
        return []
    return res
dependecies = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
jobs = [1,2,3,4]
print(topological(dependecies,jobs))




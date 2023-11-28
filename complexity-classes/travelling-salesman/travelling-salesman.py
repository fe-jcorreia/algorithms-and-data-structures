def travellingSalesmanProblem(n, dist):
    memo = {}
 
    def tsm(i, nodes):
        if not len(nodes):
            return dist[1][i]

        if memo.get((i, nodes), -1) != -1:
            return memo[(i, nodes)]
    
        res = 10**9
        for j in nodes:
            newNodes = list(nodes)
            newNodes.remove(j)
            res = min(res, tsm(j, tuple(newNodes)) + dist[j][i])
        
        memo[(i, nodes)] = res
        return res

    return tsm(1, (2,3,4))

ans = travellingSalesmanProblem(
    n = 4,
    dist = [[0, 0,  0,  0,  0],
            [0, 0, 10, 15, 20], 
            [0, 5,  0,  9, 10], 
            [0, 6, 13,  0, 12], 
            [0, 8,  8,  9,  0]])
print("The cost of most efficient tour = " + str(ans))

ans = travellingSalesmanProblem(
    n = 4,
    dist = [[0, 0,  0,  0,  0],
            [0, 0, 10, 15, 20],
            [0, 10, 0, 25, 25], 
            [0, 15, 25, 0, 30], 
            [0, 20, 25, 30, 0]])
print("The cost of most efficient tour = " + str(ans))


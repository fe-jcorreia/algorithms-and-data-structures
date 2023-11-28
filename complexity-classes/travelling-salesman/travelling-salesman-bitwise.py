
n = 4
dist = [[0, 0,  0,  0,  0],
        [0, 0, 10, 15, 20], 
        [0, 5,  0,  9, 10], 
        [0, 6, 13,  0, 12], 
        [0, 8,  8,  9,  0]]
memo = [[-1] * (1 << (n + 1)) for _ in range(n + 1)]
 
def tsm(i, mask):
    if mask == ((1 << i) | 3):
        return dist[1][i]

    if memo[i][mask] != -1:
        return memo[i][mask]
 
    res = 10**9
    for j in range(1, n + 1):
        if (mask & (1 << j)) != 0 and j != i and j != 1:
            res = min(res, tsm(j, mask & (~(1 << i))) + dist[j][i])
    memo[i][mask] = res
    return res

ans = 10**9
for i in range(1, n + 1):
    ans = min(ans, tsm(i, (1 << (n + 1)) - 1) + dist[i][1])
 
print("The cost of most efficient tour = " + str(ans))


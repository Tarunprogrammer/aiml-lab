def monkey(grid):
    r,c=len(grid),len(grid[0])
    dp=[row[:] for row in grid]
    for i in range(1,r):
        for j in range(c):
            dp[i][j]+=max(dp[i-1][max(0,j-1)],dp[i-1][j],dp[i-1][min(c-1,j+1)])
    return max(dp[-1])

g=[[1,2,3],[4,5,6],[7,8,9]]
print("Max bananas:",monkey(g))
class Solution:
    def maxDistance(self, grid):

        land=[]
        n=len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    land.append([i+1,j+1])
        if len(land)==0 or len(land)==n*n:
            return -1
        else:
            x=0
            y=0
            for k in land:
                pass

a=Solution()

print(a.maxDistance([[1,0,1],[0,0,0],[1,0,1]]))
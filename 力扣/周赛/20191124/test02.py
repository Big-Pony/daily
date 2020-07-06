class Solution:
    def countServers(self, grid):
        services=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    if i==0 and j==0:
                        if grid[i+1][j]+grid[i][j+1]>=1:
                            services+=1
                    elif i==0 and j!=0 and j!=len(grid[i])-1:
                        if grid[i+1][j]+grid[i][j+1]+grid[i][j-1]>=1:
                            services+=1
                    elif i==0 and j==len(grid[i])-1:
                        if grid[i][j-1]+grid[i+1][j]>=1:
                            services+=1
                    elif i!=0 and i!=len(grid)-1 and j==0:
                        if grid[i][j+1]+grid[i+1][j]+grid[i-1][j]>=1:
                            services+=1
                    elif i!=0 and j!=0 and i!=len(grid)-1 and j!=len(grid[i])-1:
                        if grid[i+1][j]+grid[i][j+1]+grid[i][j-1]+grid[i-1][j]>=1:
                            services+=1
                    elif j==len(grid[i])-1 and i!=0 and i!=len(grid)-1:
                        if grid[i+1][j]+grid[i][j-1]+grid[i-1][j]>=1:
                            services+=1
                    elif i==len(grid)-1 and j!=len(grid[i])-1:
                        if grid[i][j+1]+grid[i-1][j]>=1:
                            services+=1
                    elif i==len(grid)-1 and j==len(grid[i])-1:
                        if grid[i][j-1]+grid[i-1][j]>=1:
                            services+=1
                else:
                    pass
        print(services)
a=Solution()
a.countServers([[1,0,0,1,0],[0,0,0,0,0],[0,0,0,1,0]])
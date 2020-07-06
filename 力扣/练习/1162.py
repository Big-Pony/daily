class Solution:
    def maxDistance(self, grid):
        ocean=[]
        land=[]
        n=len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    ocean.append([i,j])
                else:
                    land.append([i,j])
        if len(ocean)==0 or len(land)==0:
            return -1
        distance=0
        for o in ocean:
            min_distance=9999
            for l in land:
                y=abs(o[0]-l[0])+abs(o[1]-l[1])
                if y<min_distance:
                    min_distance=y
            if min_distance>distance:
                distance=min_distance
        return distance

a=Solution()

print(a.maxDistance([[1,0,1],[0,0,0],[1,0,1]]))
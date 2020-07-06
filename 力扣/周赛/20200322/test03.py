
class Solution:
    def hasValidPath(self, grid):
        mat = {1: [3], 2: [3,4,5,6], 3: [5, 6], 4: [1, 5, 6,3], 5: [2,3,4], 6: [1,5,3,2,4]}
        m=len(grid)-1
        n=len(grid[0])-1
        dx=[0,1,-1]
        dy=[1,0,0]
        def judge(x,y,last_point):

            if  x<0 or y<0 or x > m or y > n:
                return False

            elif grid[x][y] in mat[last_point]:
                print('测试', x, y)
                return True
            else:
                return False


        def dfs(x,y,condition):
            if [x,y]==[m,n]:
                condition=True
                print(condition)
                return condition
            for i in range(3):
                new_x=x+dx[i]
                new_y=y+dy[i]

                if judge(new_x,new_y,grid[x][y]):
                    print('下一个点', x,y,new_x, new_y)
                    dfs(new_x,new_y,condition)
        condition=dfs(0,0,False)

        return condition

a=Solution()

print(a.hasValidPath([[2,4,3],[6,5,2]]))
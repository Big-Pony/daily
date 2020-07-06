class Solution:
    def hasValidPath(self, grid):
        to_up = {1: [], 2: [2,3,4], 3: [], 4: [], 5: [2,3,4], 6: [2,3,4]}
        to_right = {1: [1,3,5], 2: [], 3: [], 4: [1,3,5], 5: [], 6: [1,3,5]}
        to_left = {1: [1,4,6], 2: [], 3: [1,4,6], 4: [], 5: [1,4,6], 6: []}
        to_down = {1: [], 2: [2,5,6], 3: [2,5,6], 4: [2,5,6], 5: [], 6: []}
        direction=[to_up,to_left,to_down,to_right]
        #上、左、下、右
        dx=[-1,0,1,0]
        dy=[0,-1,0,1]
        m=len(grid)-1
        n=len(grid[0])-1
        def judge(x,y,last_point_val,path,direction):
            #print('记录',path)
            #越界
            if x<0 or y<0 or x>m or y>n:
                # print('判断越界')
                return False
            #在本次路径中走过该点
            elif [x,y] in path:
                # print('判断走过')
                return False
            #该点与上一个节点不联通
            elif grid[x][y] not in direction[last_point_val]:
                # print('判断不联通',grid[x][y],direction[last_point_val])
                return False
            else:
                return True

        def dfs(x,y,path,result):
            if [x,y]==[m,n]:
                result[0]=True
            for i in range(4):
                if result[0]:
                    break
                last_x=x+dx[i]
                last_y=y+dy[i]
                unicom=direction[i]
                # print('测试', [x, y], [last_x, last_y])
                if judge(last_x,last_y,grid[x][y],path,unicom):

                    path.append([last_x,last_y])
                    dfs(last_x,last_y,path,result)
                    # 回溯

                    if len(path) > 1:
                        path.pop()


        result=[False]
        path=[[0,0]]
        dfs(0,0,path,result)
        return result[0]
a=Solution()
print(a.hasValidPath([[1,2,1],[1,2,1]]))
print(a.hasValidPath([[2,4,3],[6,5,2]]))
print(a.hasValidPath([[1,1,1,1,1,1,3]]))


class Solution:
    def gameOfLife(self, board):
        n=len(board)-1
        m=len(board[0])-1
        dx=[-1,-1,0,1,1, 1, 0,-1]
        dy=[0 , 1,1,1,0,-1,-1,-1]
        live=[]
        die=[]
        def judge(x,y):
            if x<0 or y<0 or x>n or y>m:
                return False
            else:
                return True
        def count(x,y):
            num=0
            for i in range(8):
                new_x=x+dx[i]
                new_y=y+dy[i]
                if judge(new_x,new_y):
                    if board[new_x][new_y]==1:
                        num+=1
            val=board[x][y]
            if val==1:
                if num<2 or num>3:
                    die.append([x,y])
            else:
                if num==3:
                    live.append([x,y])
        for i in range(n+1):
            for j in range(m+1):
                count(i,j)
        for i in live:
            board[i[0]][i[1]]=1
        for i in die:
            board[i[0]][i[1]]=0
        return board
board=[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
a=Solution()
print(a.gameOfLife(board))
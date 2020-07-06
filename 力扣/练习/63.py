class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)  # 行
        m = len(obstacleGrid[0])  # 列
        if n == 1 and m == 1:
            if obstacleGrid[0][0] == 0:
                return 1
            else:
                return 0
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        db = [[0] * m for i in range(n)]
        dx = [-1, 0]
        dy = [0, -1]

        if n > 1:
            db[1][0] = 1
        if m > 1:
            db[0][1] = 1

        def judge(x, y):
            if (x, y) in {(0, 0), (0, 1), (1, 0)}:
                return False
            return True

        def judge_t(x, y):
            if x < 0 or y < 0 or x > n - 1 or y > m - 1:
                return False
            elif obstacleGrid[x][y] == 1:
                return False
            return True

        for x in range(n):
            for y in range(m):
                if obstacleGrid[x][y] == 0 and judge(x, y):
                    top_x, top_y = x - 1, y
                    left_x, left_y = x, y - 1

                    if judge_t(top_x, top_y):
                        db[x][y] += db[top_x][top_y]
                    if judge_t(left_x, left_y):
                        db[x][y] += db[left_x][left_y]
        return db[-1][-1]
martix=[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
a=Solution()
a.uniquePathsWithObstacles(martix)


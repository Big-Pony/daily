class Solution:
    def luckyNumbers (self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        max_row=[0 for i in range(n)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]>max_row[j]:
                    max_row[j]=matrix[i][j]
        lucky=[]
        for i in range(m):
            min_val=min(matrix[i])
            min_ind=matrix[i].index(min_val)
            if min_val>=max_row[min_ind]:
                lucky.append(min_val)
        return lucky

a=Solution()

print(a.luckyNumbers( [[3,7,8],[9,11,13],[15,16,17]]))
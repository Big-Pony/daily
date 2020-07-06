class Solution:
    def rotate(self, matrix):
        import math
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        half=math.ceil(n/2)
        print(n,half)
        for i in range(n):
            for j in range(i,n):

                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            for k in range(half,n):
                matrix[i][k],matrix[i][n-k-1]=matrix[i][n-k-1],matrix[i][k]

        print(matrix)
matrix = \
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
a=Solution()
#a.rotate(matrix)
a.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])

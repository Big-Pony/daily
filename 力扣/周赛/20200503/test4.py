class Solution:
    def kthSmallest(self, mat, k):
        import math
        m=len(mat)
        n=len(mat[0])
        serach=[n**(m-i) for i in range(1,m+1)]
        res=0
        print(serach)
        for j in range(m):
            if j<m-1:
                print(mat[j][math.ceil(k / serach[j]) - 1])
                res+=mat[j][math.ceil(k/serach[j])-1]
            else:

                res+=mat[j][k%n-1]
        return res

a=Solution()

print(a.kthSmallest(mat = [[1,3,11],[2,4,6]], k = 5))
print(a.kthSmallest([[1,10,10],[1,4,5],[2,3,6]],k=7))

'''
    math.celi(k/n)
    
    k//n
'''
class Solution:
    def lastRemaining(self, n, m):
        lis =list(range(n))
        if m==1:
            return lis[-1]
        i=0
        while n>1:
            i=(i+m-1)%n
            lis.pop(i)
            n-=1
        return lis[0]

a=Solution()

print(a.lastRemaining(5,3))

print(a.lastRemaining(10,17))
# 0 1 2 3 4
#0 1 2 3 4 5  7 8 9

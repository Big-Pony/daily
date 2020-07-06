class Solution:
    def countTriplets(self, arr):
        from functools import reduce
        n=len(arr)
        res=0
        def yh(x,y):
            return x^y
        for i in range(0,n):
            for j in range(i+1,n):
                a = reduce(yh, [arr[m] for m in range(i, j)])
                for k in range(j,n):

                    b=reduce(yh,[arr[m] for m in range(j,k+1)])
                    if a==b:
                        res+=1

        return res


a=Solution()
print(a.countTriplets(arr = [2,3,1,6,7]))
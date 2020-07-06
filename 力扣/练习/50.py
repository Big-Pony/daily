class Solution:
    def myPow(self, x, n):
        fu=False
        if n <0:
            fu=True
            n=-n
        k=1
        db={1:x}
        while k<n:
            c=k*2
            db[c]=db[k]*db[k]
            k=c
        res=1
        serach=bin(n)
        ind=1

        for i in range(-1,-len(serach)+1,-1):
            if serach[i]=='1':
                res*=db[ind]
            ind *= 2

        return 1/res if fu else res
a=Solution()
# print(a.myPow(2,10))
# print(a.myPow(2,-10))
# print(a.myPow(0,10))
print(a.myPow(2.00000,-2))


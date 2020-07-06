class Solution:
    def buildArray(self, target, n):
        lis=[i for i in range(1,n+1)]
        n=len(lis)
        m=len(target)
        res=[]
        his=set()
        for i in range(m):

            for j in range(i,n):
                if j not in his:
                    res.append('Push')
                    if target[i]==lis[j]:
                        if j not in his:
                            his.add(j)
                        break
                    else:
                        if j not in his:
                            his.add(j)
                        res.append('Pop')

        return res

a=Solution()
print(a.buildArray(target = [1,3], n = 3))
print(a.buildArray(target = [1,2,3], n = 3))
print(a.buildArray(target = [1,2], n = 4))
print(a.buildArray(target = [2,3,4], n = 4))
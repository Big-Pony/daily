#5297,
class Solution:
    def canReach(self, arr, start):
        n=len(arr)
        if not arr or start>n-1:
            print('false')
            return False
        if arr[start]==0:
            print('true')
            return True
        tree=[[start]]
        jihe=[start]
        i=-1

        while True:
            i+=1
            lis=[]
            for j in tree[i]:
                a=j + arr[j]
                b=j - arr[j]
                if 0<=a<=n-1 and a not in jihe :
                    lis.append(a)
                if 0<=b<=n-1 and b not in jihe :
                    lis.append(b)
            if len(lis)==0:
                print('false')
                return False
            tree.append(lis)
            jihe.extend(lis)
            if 0 in [arr[x] for x in tree[i+1]]:
                print('true')
                return True

a=Solution()
#a.canReach(arr = [4,2,3,0,3,1,2], start = 5)#true
#a.canReach(arr = [4,2,3,0,3,1,2], start = 0)#true
a.canReach(arr = [3,0,2,1,2], start = 2)#false

a.canReach([0,3,0,6,3,3,4],6)#true
a.canReach([0],0)#true



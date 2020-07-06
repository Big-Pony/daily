class Solution1:
    def maxDepthAfterSplit(self, seq):
        n=len(seq)
        res=[0 for i in range(n)]
        count=n
        left=0
        jo=0
        right=0
        while count>0:
            for j in range(left,n):
                if seq[j]=='(':
                    left=j
                    break
            for j in range(right,n):
                if seq[j]==')':
                    right=j
                    break
            count-=2
            if jo==0:
                jo=1
                left+=1
                right+=1
            else:
                res[left]=1
                res[right]=1
                jo=0
                left+=1
                right+=1

        return res


a=Solution1()
print(a.maxDepthAfterSplit("(()())"))
print(a.maxDepthAfterSplit("()(())()"))
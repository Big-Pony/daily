class Solution:
    def findJudge(self, N, trust):
        if N==1:
            return 1
        if N<1:
            return -1

        cm=set()
        fg=set()
        for i in trust:
            cm.add(i[0])
            fg.add(i[1])
        fg=fg-cm
        if len(fg)<1:
            return -1
        else:
            fg=list(fg)
            for j in range(len(fg)):
                judge=0
                for i in range(1,N+1):
                    if i==fg[j]:continue
                    else:
                        if [i,fg[j]] in trust:
                            pass
                        else:
                            judge=1
                if judge==0:
                    return fg[j]
                else:
                    return -1



a=Solution()
a.findJudge(4,[[1,3],[1,4],[2,3],[2,4],[4,3]])
a.findJudge(3, [[1,2],[2,1]])
class Solution:
    def rankTeams(self, votes):
        if len(votes)==1:
            return votes[0]
        n=len(votes[0])
        scor={}
        for i in range(len(votes)):
            for j in range(n):
                if votes[i][j] not in scor:
                    scor[votes[i][j]]=[0 for k in range(n)]
                    #[0,0,0]
                    scor[votes[i][j]][j]+=1
                else:
                    scor[votes[i][j]][j] += 1
        print(scor.items())

        scor=[p for p in sorted(scor.items(),key=lambda item:item[0])]

        result_lis=[p for p in sorted(scor,key=lambda item:[-item[1][m] for m in range(n)])]

        result=''
        for i in result_lis:
            result+=i[0]
        print(result)
        return result

a=Solution()
a.rankTeams(["ABC","ACB","ABC","ACB","ACB"])

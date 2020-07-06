class Solution:
    def rankTeams(self, votes):
        if len(votes)==1:
            return votes[0]

        result = ''
        for i in range(len(votes[0])):
            scor = {}
            for j in range(len(votes)):
                if votes[j][i] not in scor:
                    scor[votes[j][i]] = 1
                else:
                    scor[votes[j][i]] += 1
            result_lis=[i for i in sorted(scor.items(),key=lambda item:(-item[1],item[0]))]
            print(result_lis)
            if len(result)==len(votes[0]):
                break
            for k in result_lis:
                if k[0] not in result:
                    result+=k[0]



        print(result)
        return result




a=Solution()
a.rankTeams(["WXYZ","XYZW"])

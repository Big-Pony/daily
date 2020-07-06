class Solution:
    def destCity(self, paths):
        roads = paths[0]
        n = len(paths)
        while len(roads) < n+1:
            for i in range(n):

                if paths[i][0] == roads[-1]:
                    roads.append(paths[i][1])
                elif paths[i][1] == roads[0]:
                    roads.insert(0,paths[i][0])
        return roads

a=Solution()

#print(a.destCity([["B","C"],["D","B"],["C","A"]]))
print(a.destCity([["rPKvGbYzi ","SjQteUGNpU"],["SjQteUGNpU","CBAySumUcZ"]]))
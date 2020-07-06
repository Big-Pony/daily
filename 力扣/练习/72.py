class Solution:
    def minDistance(self, word1, word2):
        word2 = ' ' + word2
        word1 = ' ' + word1
        n=len(word1)
        m=len(word2)
        db = [[0] * n for i in range(m)]
        def judge(i,j):
            if i==0 and j==0:
                return 0
            elif i==0:
                return db[i][j-1]
            elif j==0:
                return db[i-1][j]
            else:
                return min(db[i-1][j-1],db[i-1][j],db[i][j-1])
        for i in range(m):

            for j in range(n):
                if word2[i]==word1[j]:
                    db[i][j]=db[i-1][j-1]

                else:
                    db[i][j] = judge(i,j)+1

        return db[-1][-1]

a=Solution()
print(a.minDistance(word1 = "horse", word2 = "ros"))
print(a.minDistance(word1 = "intention", word2 = "execution"))
print(a.minDistance("zoologicoarchaeologist","zoogeologist"))

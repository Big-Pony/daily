class Solution:
    def minTime(self, n, edges, hasApple):
        global res
        res = []
        global road
        road={}
        for i in edges:
            if i[0] not in road:
                road[i[0]]=[i[1]]
            else:
                road[i[0]].append(i[1])
        def dfs(start, path):
            global road
            if start in road:
                for i in road[start]:

                    if i not in path:
                        path.append(i)
                        dfs(i, path)

            if (hasApple[start]):
                res.extend(path)
            if len(path) > 0:
                path.pop()

        dfs(0, [])


        return len(set(res))*2

a=Solution()
print(a.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,True,True,False]))
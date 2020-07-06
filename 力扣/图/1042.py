class Solution:
    def gardenNoAdj(self, N, paths):
        p_map={i:[] for i in range(1,N+1)}
        seed={i:0 for i in range(1,N+1)}

        for i in paths:
            if i[1] not in p_map[i[0]]:
                p_map[i[0]].append(i[1])
            if i[0] not in p_map[i[1]]:
                p_map[i[1]].append(i[0])

        for i in p_map.keys():
            all_seed = [1, 2, 3, 4]
            side=p_map[i]
            if len(side)<1:
                seed[i]=1
            else:

                for j in side:
                    if seed[j]==0:
                        continue
                    else:
                        if seed[j] not in all_seed:
                            continue
                        else:
                            ind=all_seed.index(seed[j])
                            del all_seed[ind]

                seed[i]=all_seed[0]


        return [k for k in seed.values()]


a=Solution()
a.gardenNoAdj(4,[[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]])
a.gardenNoAdj(5,[[4,1],[4,2],[4,3],[2,5],[1,2],[1,5]])


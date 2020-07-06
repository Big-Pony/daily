class Solution:
    def minTimeToVisitAllPoints(self, points):
        times=0
        for i in range(len(points)-1):
            last_point=points[i]
            next_point=points[i+1]
            x0=abs(next_point[0]-last_point[0])
            y0=abs(next_point[1]-last_point[1])
            if x0>y0:
                times+=y0+(x0-y0)
            if x0<y0:
                times+=x0+(y0-x0)
            if x0==y0:
                times+=x0
        print(times)
a=Solution()
a.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])

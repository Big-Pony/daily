class Solution1:
    def trap(self, height):
        if len(height)<1:
            return 0
        total=0
        n=len(height)
        max_height=max(height)
        for i in range(1,max_height+1):
            left=0
            full=set()
            for j in range(0,n):
                if height[j]>=i:
                    full.add(j)
            all_gezi=set(range(min(full),max(full)+1))
            total+=len(all_gezi-full)

        return total
class Solution2:
    def trap(self, height):
        n=len(height)
        l=-1
        l_max=0
        r=n
        r_max=0
        l_list=[]
        r_list=[]
        total=0
        while l<n-1:
            l+=1
            r-=1
            #print(l,r)
            l_max=max(l_max,height[l])
            r_max=max(r_max,height[r])
            l_list.append(l_max)
            r_list.append(r_max)
        for i in range(n):
            total+=min(l_list[i],r_list[n-i-1])-height[i]
        return total

a=Solution2()
print(a.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(a.trap([2,0,2]))
print(a.trap([5,4,1,2]))
print(a.trap([5,2,1,2,1,5]))


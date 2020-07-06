class MountainArray:
    def __init__(self,lis=[]):
        self._lis=lis
    def get(self, index):
        return self._lis[index]
    def length(self) -> int:
        return len(self._lis)
class Solution:
    def findInMountainArray(self, target, mountain_arr):
        n=mountain_arr.length()
        l=0
        r=n-1
        max_height=None
        while max_height==None:
            middle=(l+r)//2
            middle_val=mountain_arr.get(middle)
            middle_last=mountain_arr.get(middle-1)
            middle_next=mountain_arr.get(middle+1)
            if middle_last<middle_val>middle_next:
                max_height=middle
                break
            elif middle_last<middle_val:
                l=middle
            else:
                r=middle

        #sortlis,表示l到r为升序还是降序，升序为True，降序为False
        print('测试',max_height)
        def search(l,r,sortlis):
            if l==r:
                if mountain_arr.get(l)==target:
                    return l
                else:
                    return -1
            if l<r:
                middle = (l + r) // 2
                middle_val=mountain_arr.get(middle)
                if middle_val==target:
                    return middle
                elif sortlis:
                    if middle_val > target:
                        return search(l,middle,sortlis)
                    else:
                        return search(middle+1, r, sortlis)
                else:
                    if middle_val > target:
                        return search(middle+1, r, sortlis)
                    else:
                        return search(l, middle, sortlis)
            else:
                return -1

        res=search(0,max_height,True)
        if res==-1:
            return search(max_height+1,n-1, False)
        else:
            return res


mountain_arr=MountainArray([0,5,3,1])

a=Solution()
print(a.findInMountainArray(3,mountain_arr))



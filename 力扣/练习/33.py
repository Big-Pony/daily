import time
class Solution:
    def search(self, nums, target):
        n=len(nums)
        max_val=max(nums)
        max_ind=nums.index(max_val)
        if n<2:
            if (target in nums):
                return 0
            else:
                return -1
        if target<=nums[-1]:

            for i in range(-1,-max_ind-1,-1):
                if nums[i]==target:
                    return n+i

        elif target>=nums[0]:
            for i in range(0,max_ind+1):
                if nums[i]==target:
                    return i
        else:
            return -1

# a=Solution()
# print(a.search(nums = [4,5,6,7,0,1,2], target = 0))

class Solution1:
    def search(self, nums, target):
        n=len(nums)
        if n<1:
            return -1
        max_val=max(nums)
        middle=nums.index(max_val)

        l=0
        r=n-1
        if target==max_val:
            return middle
        elif target>=nums[0]:
            r = middle - 1
        elif target<nums[0]:
            l = middle + 1



        while l<=r:
            middle=(l+r)//2
            m_val=nums[middle]
            if m_val==target:
                return middle
            elif target>m_val:
                l=middle+1
            else:
                r=middle-1

        return -1



start=time.time()
a=Solution1()
#print(a.search(nums = [4,5,6,7,0,1,2], target = 10))
print(a.search([6,7,1,2,3,4,5],6))
end=time.time()
print(end-start)


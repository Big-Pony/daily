class Solution:
    def minSubsequence(self, nums):
        res=0
        nums=sorted(nums,reverse=True)

        ind=0
        for i in range(len(nums)):
            if res<=sum(nums[i:]):
                res+=nums[i]
                if i==len(nums)-1:
                    ind=i+1

            else:
                ind=i
                break

        return nums[:ind]

a=Solution()

print(a.minSubsequence([4,3,10,9,8]))
print(a.minSubsequence([4,4,7,6,7]))
print(a.minSubsequence([6]))
print(a.minSubsequence([1,7,4,7,1,9,4,8,8]))

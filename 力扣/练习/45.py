class Solution:
    def jump(self, nums):
        n = len(nums)
        #记录到某个点的最少步数
        db=[0]
        for i in range(n):
            ldb=len(db)
            for j in range(ldb,i+nums[i]+1):

                if ldb-1<j<n:db.append(db[i]+1)

        return db[-1]

a=Solution()

print(a.jump([2,3,1,1,4]))
print(a.jump([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]))
print(a.jump([1,2]))
print(a.jump([1,2,3]))
print(a.jump([2,3,0,1,4]))
print(a.jump([3,2,1]))

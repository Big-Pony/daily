class Solution:
    def sortArray(self, nums):
        def replace(arr, start, end):
            base = start
            base_val = arr[start]
            left = start + 1
            right = end

            while True:
                while left < right and arr[left] <= base_val:
                    left += 1

                while right > left and arr[right] > base_val:
                    right -= 1

                if left == right:
                    if arr[left] < base_val:
                        arr[left], arr[base] = arr[base], arr[left]
                    else:
                        arr[left - 1], arr[base] = arr[base], arr[left - 1]
                    break

                else:
                    arr[left], arr[right] = arr[right], arr[left]
            return left

        def quick_sort(arr, start, end):
            if start < end:
                middle = replace(arr, start, end)
                quick_sort(arr, start, middle - 1)
                quick_sort(arr, middle, end)

        quick_sort(nums, 0, len(nums) - 1)
        return nums

a=Solution()
print(a.sortArray([5,9,3,1,6,8,7,12]))
print(a.sortArray([5,2,3,1]))


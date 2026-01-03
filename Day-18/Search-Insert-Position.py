# Question from : https://leetcode.com/problems/search-insert-position/description/

def searchInsert(nums, target) -> int:
        left = 0
        right = len(nums) - 1

        while(left<=right):
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        
        return left

nums = [1,3,5,6]
target = 5
# target = 2
# target = 7

idx = searchInsert(nums,target)
print(idx)

########################################################################################
# Time complexity is O(logn)
# Space complexity is O(1)
########################################################################################

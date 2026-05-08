class Solution:
   def twoSum(self, nums, target):
    # Check each number one by one
    for i in range(len(nums)):
        # Check every number after it
        for j in range(i + 1, len(nums)):
            # If these two numbers add up to target
            if nums[i] + nums[j] == target:
                return [i, j]

# Test it
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
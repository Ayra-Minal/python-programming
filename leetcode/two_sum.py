        

class Solution():
    def twoSum(self,nums,target):
        seen={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in seen:
                return (seen[diff],i)
            else:
                seen[nums[i]]=i
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range (len(nums)):
            diff = target - nums[i]
            if diff in nums[i+1:]:
                return [i,nums.index(diff,i+1)]
"""            
nums = [1,2,3,4]
target=6
sol=Solution()
ans=sol.twoSum(nums,target)
print(ans)               
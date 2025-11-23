#majority element
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate  = None
        count = 0
        for num in nums:
            if count==0:
                candidate=num
            if candidate == num:
                count+=1
            else:
                count-=1
        if nums.count(candidate)>len(nums)//2:
            return candidate                
        return None    

from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        c = Counter(nums)
        avg = len(nums)//3
        res=[]
        print(c)
        for key, item in c.items():
            if item>avg:
                res.append(key)
        return res      
    
if __name__ == "__main__":
    sol=Solution()
    nums=[1,2,1]
    print("output is:",sol.majorityElement(nums))    
""" 
Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 


#or use Counter from Collections package
from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        c = Counter(nums)
        avg = len(nums)//2
        for key, item in c.items():
            if item>avg:
                return key
"""      


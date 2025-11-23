'''
class Solution():
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen ={}
        i=0
        left = 0
        maxlen=[]
        seen(s[left])==i
        for i in range (1,len(s)):
            current=i
            if s[i] not in seen:
                seen(s[i])==i
            else:
                maxlen.append(current-left)
                left+=1
        return max(maxlen)        
'''    
class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        maxlen = 0
        
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            maxlen = max(maxlen, right - left + 1)
        
        return maxlen

if __name__ == "__main__":
    s = "abcdabcbb"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))  # Output: 3

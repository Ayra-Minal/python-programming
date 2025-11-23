from collections import defaultdict
class Solution:
    def groupanagram(self,strs):
        groups = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            groups[key].append(word)
        return list(groups.values())    

if __name__=='__main__':
    sol=Solution()
    strs=["eat","tea","tan","ate","nat","bat"]
    print(sol.groupanagram(strs))          
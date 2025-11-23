
#1.two sum
class Solution():
    def twoSum(self,nums,target):
        seen={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in seen:
                return (seen[diff],i)
            else:
                seen[nums[i]]=i       
if __name__=="__main__":
    nums=[2,7,11,15]
    target=9
    sol=Solution()
    print(sol.twoSum(nums,target))  # Output: (0, 1)
---------------------------------------------------------------------------------------
#2.valid parenthesis
class Solution(object):
    def isValid(self, s):
        stack=[]
        for char in s:
            if char in '[{(':
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if ((char == ')' and top!='(') or (char == '}' and top!='{') or (char == ']' and top!='[')):
                    return False
        return not stack             
if __name__=="__main__":
    s = "({[]})"
    sol = Solution()
    print(sol.isValid(s))  # Output: True

-----------------------------------------------------------------------------------------------------
#3.longest substring without repeating characters
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
    print(sol.lengthOfLongestSubstring(s))  # Output: 4

-----------------------------------------------------------------------------------------------------
#4.product of array except self without division
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n
        
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i] 

        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    sol = Solution()
    print(sol.productExceptSelf(nums))  # Output: [24, 12, 8, 6]    
----------------------------------------------------------------------------------------------------
#5.merge intervals
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        merged=[]
        for interval in intervals:
            if not merged or interval[0]>merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1]=max(merged[-1][1],interval[1])
        return merged 

if __name__=="__main__":
    intervals=[[1,3],[2,6],[8,10],[15,18]]
    sol=Solution()
    print(sol.merge(intervals))  # Output: [[1, 6], [8, 10], [15, 18]]
-----------------------------------------------------------------------------------------------------
#6.reverse a linked list
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next     # 1️⃣ store next
            curr.next = prev          # 2️⃣ reverse the link
            prev = curr               # 3️⃣ move prev forward
            curr = next_node          # 4️⃣ move curr forward
        
        return prev  
    
if __name__=="__main__":
    # Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    sol = Solution()
    reversed_head = sol.reverseList(head)

    # Print reversed linked list
    curr = reversed_head
    while curr:
        print(curr.val, end=" -> " if curr.next else "")
        curr = curr.next
    # Output: 5 -> 4 -> 3 -> 2 -> 1    

----------------------------------------------------------------------------------------------------
#7.find townjudge
# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
# # The town judge trusts nobody.
# # Everybody (except for the town judge) trusts the town judge.
# Input: n = 2, trust = [[1,2]]
# Output: 2
# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3

class Solution(object):
    def findJudge(self, n, trust):
        # if there's only one person and no trust relation, that person is judge
        if n == 1 and not trust:
            return 1
        
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)
        
        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1
        
        for i in range(1, n + 1):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i
        
        return -1

if __name__=="__main__":
    n = 3
    trust = [[1,3],[2,3]]
    sol = Solution()
    print(sol.findJudge(n, trust))  # Output: 3
---------------------------------------------------------------------------------------------------

#8.Binary Tree Level Order Traversal
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level_size=len(queue)
            level_node=[]

            for i in range (level_size):
                node=queue.popleft()
                level_node.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)  
            result.append(level_node)          
        return result
if __name__=="__main__":
    # Creating a binary tree:
    #       3
    #      / \
    #     9  20
    #        / \
    #       15  7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    print(sol.levelOrder(root))  # Output: [[3], [9, 20], [15, 7]]            

    

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(levels):
    if not levels or not levels[0]:
        return None

    root = TreeNode(levels[0][0])
    queue = deque([root])

    for level in levels[1:]:
        new_queue = deque()
        i = 0
        while queue and i < len(level):
            node = queue.popleft()

            if i < len(level):
                node.left = TreeNode(level[i])
                new_queue.append(node.left)
                i += 1

            if i < len(level):
                node.right = TreeNode(level[i])
                new_queue.append(node.right)
                i += 1

        queue = new_queue

    return root

if __name__ == "__main__":
    levels = [
        [3],
        [9, 20],
        [15, 7]
    ]
    root = buildTree(levels)
----------------------------------------------------------------------------------------------------
#9. longest consecutive sequence
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset=set(nums)
        longest=0
        for n in numset:
            if(n-1) not in numset:
                length=1
                while (n+length)in numset:
                    length+=1
                longest=max(length,longest)
        return longest            
if __name__=="__main__":
    nums = [100, 4, 200, 1, 3, 2]
    sol = Solution()
    print(sol.longestConsecutive(nums))  # Output: 4  
---------------------------------------------------------------------------------------------------
    
#10.subarray sum equals k  
class Solution(object):
    def subarraySum(self, nums, k):
        prefix_sum=0
        count=0
        freq={0,1}
        for num in nums:
            prefix_sum+=num

            if(prefix_sum-k)in freq:
                count+=freq[prefix_sum-k]

            freq[prefix_sum]=freq.get(prefix_sum,0)+1
        return count        
    
    
if __name__=="__main__":
    nums = [1, 1, 1]
    k = 2
    sol = Solution()
    print(sol.subarraySum(nums, k))  # Output: 2             
---------------------------------------------------------------------------------------------------
#11 rotten oranges
from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # Step 1: Find initial rotten and count fresh
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # No fresh oranges
        if fresh == 0:
            return 0

        minutes = -1  # start from -1 since we count after processing each layer
        directions = [(1,0), (-1,0), (0,1), (0,-1)]#d,u,r,l

        # Step 2: BFS
        while queue:
            minutes += 1
            for _ in range(len(queue)):  # one level = one minute
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2   # now rotten
                        fresh -= 1
                        queue.append((nr, nc))

        # Step 3: Check remaining fresh oranges
        return minutes if fresh == 0 else -1
    
if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    sol = Solution()
    print(sol.orangesRotting(grid))  # Output: 4
--------------------------------------------------------------------------------------------------
#12.number of islands
class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            # base case: out of bounds or water
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return

            # mark as visited (turn land into water)
            grid[r][c] = "0"

            # explore all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # main loop
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1     # found new island
                    dfs(r, c)        # sink it (mark visited)
        return islands
    
if __name__ == "__main__":
    grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    sol = Solution()
    print(sol.numIslands(grid))  # Output: 3
--------------------------------------------------------------------------------------------------
#13.course schedule
from collections import defaultdict, deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        adj = defaultdict(list)  # ✅ auto-handles missing keys
        indegree = [0] * numCourses

        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
         
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        taken = 0

        while queue:
            course = queue.popleft()
            taken += 1
            for neighbor in adj[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return taken == numCourses
if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1,0]]
    sol = Solution()
    print(sol.canFinish(numCourses, prerequisites))  # Output: True    
--------------------------------------------------------------------------------------------------
#14.Merge Two Sorted Lists
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        new_node = ListNode()   # dummy node to start the new list
        tail = new_node         # tail always points to the last node in merged list

        # while both lists have nodes
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1     # attach list1 node
                list1 = list1.next    # move list1 forward
            else:
                tail.next = list2     # attach list2 node
                list2 = list2.next    # move list2 forward
            tail = tail.next          # move tail forward

        # if one list still has nodes, attach it
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return new_node.next             # head of merged list
    
if __name__=="__main__":
    # Creating first sorted linked list: 1 -> 2 -> 4
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)

    # Creating second sorted linked list: 1 -> 3 -> 4
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    sol = Solution()
    merged_head = sol.mergeTwoLists(list1, list2)

    # Print merged linked list
    curr = merged_head
    while curr:
        print(curr.val, end=" -> " if curr.next else "")
        curr = curr.next
    # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4    

--------------------------------------------------------------------------------------------------
#15.symmetric tree
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        # If the tree is empty, it's symmetric
        if not root:
            return True
        
        # helper function to check if two trees are mirrors
        def isMirror(t1, t2):
            # both null -> symmetric
            if not t1 and not t2:
                return True
            
            # one is null, other isn't -> not symmetric
            if not t1 or not t2:
                return False
            
            # check current values and mirror structure
            return (t1.val == t2.val and
                    isMirror(t1.left, t2.right) and
                    isMirror(t1.right, t2.left))
        
        # check if left and right subtrees are mirrors
        return isMirror(root.left, root.right)
if __name__=="__main__":
    # Creating a symmetric binary tree:
    #       1
    #      / \
    #     2   2
    #    / \ / \
    #   3  4 4  3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    sol = Solution()
    print(sol.isSymmetric(root))  # Output: True  
----------------------------------------------------------------------------------------------------------------         
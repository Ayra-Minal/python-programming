#Question: Coin Change (Minimum Number of Coins)
# Problem Statement:
# You are given:
# An integer array coins representing the denominations of available coins.
# An integer amount representing a target amount of money.
# Your task is to determine the minimum number of coins needed to make up the given amount.
# You may use each coin an unlimited number of times.
# If the amount cannot be made with the given coins, return -1.
class Solution:
    def coinchange(self,coins,amount):
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for i in range (1,amount+1):
            for coin in coins:
                if i-coin>=0:
                    dp[i]=min(dp[i],dp[i-coin]+1)
        return dp[amount] if dp[amount]!=float('inf') else -1            
    # Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.coinchange([1, 2, 5], 11))  # Output: 3

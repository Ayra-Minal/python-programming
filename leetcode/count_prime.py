#Algorithm Used: Sieve of Eratosthenes
# This is the FASTEST way to count primes up to a limit.
"""
class Solution:
    def prime(self,n):
        flag=True    
        for i in range (2,(n//2)+1):
            if n%i==0:
                flag=False
        if flag == False:
            print("not prime")
        else:
            print("prime")            
"""
    
class Solution:
    def countprime(self,n):
        if n <= 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        for i in range (2, int(n**0.5) + 1): 
            if is_prime[i]:
                for j in range (i*i,n,i):
                    is_prime[j]=False        
        return sum(is_prime)

if __name__ == '__main__':
    sol=Solution()
    print(sol.countprime(23))  #8

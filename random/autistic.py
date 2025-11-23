#find agustic value and find sum...if given is 125...find(1+25,12+5,1+2+5,125)ka sum

class solution:
    def agustic(self,n):
        total = 0
        l = len(n)
        num_splits = l-1

        for mask in range (2 ** num_splits):
            parts = [] #parts will store all the numbers in one combination (like ["1", "25"])
            current = n[0]

            for i in range(num_splits):
                if mask & ( 1<<i ):#if it is 1 in binary term say in 10
                    parts.append(current)
                    current = n[i+1]
                else:#0 say in 00 or 01
                    current += n[i+1]
            parts.append(current)

            total += sum(map(int,parts))            
        return total

if __name__ =='__main__':
    sol=solution()
    n = "125"
    print("final height of tree is :",sol.agustic(n))

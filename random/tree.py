#watering a tree of initial height 0 by glass having water > height of tree

class solution:
    def totheight(self,n,glass):
        tree = 0
        glass = sorted(glass)
        i = 0
        while i < n:
            if tree < glass[i]:
                tree += glass[i]
            i+=1
        return tree
if __name__ =='__main__':
    sol=solution()
    n = 5
    glass = [3,2,1,5,1]
    print("final height of tree is :",sol.totheight(n,glass))

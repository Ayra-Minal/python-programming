class solution:
    def allen(self,inp1,inp2,inp3):
        A = sorted (inp2)
        G = sorted (inp3)
        diff = [G[i]-A[i] for i in range (min(inp1,len(G)))]
        return min(diff)
    

if __name__ =='__main__':
    sol=solution()
    inp1 = 3
    inp2 = [2,1,3]
    inp3 = [2]
    print(sol.allen(inp1,inp2,inp3))
    
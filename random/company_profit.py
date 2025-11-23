#a company have many product of [cost]...need to find profit by adding values
#between L and R...L from input 3 and R from input 4


class solution:
    def profit(self,input1,input2,input3,input4,input5):
        cost=(input1 * (input2+1))
        print (cost)
        final=[]
        for i in range(input5):
            L = input3[i]
            R = input4[i]
            L -= 1
            R -= 1
            if 0 <= L <= R <= len(cost):
                total = sum(cost[L:R+1])
            else:
                total = 0
            final.append(total)    
        return final                 

if __name__ =='__main__':
    sol=solution()
    input1 = [4,1,5]
    input2 = 3
    input3 = [1,3]
    input4 = [4,7]
    input5 = 2
    print("final profit is :",sol.profit(input1,input2,input3,input4,input5))

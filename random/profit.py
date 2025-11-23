#company selling items(uniqueid) such that max profit is attained...is 2 consecutive same uniqueid..choose bigger
#input1(uniqueid):{1,2,3}
#input2 :3
#input3: {10,20,30}
#input4: 3
#output: 60

class solution:
    def totprofit(self,n,uniqueid,profit):
        ret = 0
        i = 0
        for j in range (n):
            if profit[j]<0:
                profit[j]=0
        
        while i < n:
            temp=profit[i]
            while i + 1 < n and uniqueid[i] == uniqueid[i + 1]:              
                temp=(max(temp, profit[i + 1]))
                i+=1      
            ret += temp
            i+=1
        return ret             

if __name__ =='__main__':
    sol=solution()
    n = 5
    uniqueid = [4,1,1,1,4]
    profit = [-1,10,10,15,-5]
    print("attainable profit is :",sol.totprofit(n,uniqueid,profit))

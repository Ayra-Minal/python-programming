'''
# greatest next element
def nextgreatest(input):
    output=[]
    prev = 0
    current_highest=0
    n=len(input)
    for i in range(n): 
        value=input[i]
        for j in range(i+1,n):
            if value<prev:
                output.append(current_highest)
                prev=value
                break
            while input[j]<=value:
                j+=1
            if input[j]>value:
                output.append(input[j])
                current_highest=input[j]
            if j==n-1:
                output.append(-1)
                
            
    return output        

'''



def nextgreatest(input):
    output=[]
    prev = 0
    current_highest=0
    n=len(input)
    for i in range(n):
        value=input[i]
        if i==n-1:
            output.append(-1)
        for j in range(i+1,n):
            
            if value < input[j]:
                output.append(input[j])
                current_highest=input[j]
                prev=value
                break
            else:
                j+=1
    return output


    
input =[1,3,2,4]
input2=[1,4,3,5,2]
print(nextgreatest(input))    
print(nextgreatest(input2))

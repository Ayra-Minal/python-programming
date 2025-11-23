def heapify(arr,n,i):
    largest = i
    lc = 2*i+1
    rc = 2*i+2

    if lc<n and arr[lc]>arr[largest]:
        largest = lc
    if rc<n and arr[rc]>arr[largest]:
        largest = rc
    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]
        heapify(arr,n,largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 -1,-1,-1):#last non leaf node to root heapifying
        heapify(arr,n,i)
        
    for i in range(n-1,0,-1):    
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)       
    return arr                 

print("6. Heap Sort:", heap_sort([12, 11, 13, 5, 6, 7]))
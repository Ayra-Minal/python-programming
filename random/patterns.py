'''
n=5
for i in range (n):
    for j in range(n):
        print(" * ",end='')
    print()    


 *  *  *  *  * 
 *  *  *  *  *
 *  *  *  *  *
 *  *  *  *  *
 *  *  *  *  *
 ----------------------------------------------------------------
    

n=5
for i in range (n):
    for j in range(i+1):
        print(" * ",end='')
    print()  

 * 
 *  *
 *  *  *
 *  *  *  *
 *  *  *  *  *    
---------------------------------------------------------------------


n=5
for i in range (n):
    for j in range(n-i):  #or (i,n)
        print(" * ",end='')
    print()  

 *  *  *  *  * 
 *  *  *  *
 *  *  *
 *  *
 *    
--------------------------------------------------------------------------

n=5
for i in range (n):
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i+1):
        print("*",end=' ')    
    print()  

          * 
        * *
      * * *
    * * * *
  * * * * * 
---------------------------------------------------------------------------

n=5
for i in range (n):
    for j in range(i+1):
        print(" ",end=' ') 
    for j in range(i,n):
        print("*",end=' ')   
    print() 

  * * * * * 
    * * * *
      * * *
        * *
          *
-----------------------------------------------------------------------------

n=5
for i in range (n):
    for j in range(i,n):
        print(" ",end=' ') 
    for j in range(i+1):
        print("*",end=' ')   
    for j in range(i):
        print("*",end=' ')    
    print() 

          *  
        * * *
      * * * * *
    * * * * * * * 
  * * * * * * * * * 
------------------------------------------------------------------------    
n=5
for i in range(n):
    for j in range (i+1):
        print(" ",end=' ')
    for j in range (i,n):
        print("*",end=' ')
    for j in range(i+1,n):
        print("*",end=' ')    
    print()        

  * * * * * * * * * 
    * * * * * * *
      * * * * *
        * * *
          *

---------------------------------------------------------------------------

n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    for j in range(i):
        print("*",end=' ')
    print()
for i in range(n-1):
    for j in range(i+2):
        print(" ",end=' ')
    for j in range(i+1,n):
        print("*",end=' ')
    for j in range(i+2,n):
        print("*",end=' ')    
    print()            

          * 
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * * 
    * * * * * * *
      * * * * * 
        * * *
          *
--------------------------------------------------------------------------          


n =5
for i in range(n-1): 
    for j in range(i+1):
        print("*", end=' ')
        
    for j in range(i,n-1):
        print(" ", end=' ')
        
    for j in range(i,n-1):
        print(" ", end=' ')
    for j in range(i+1):
        print("*", end=' ')
    print()
for i in range(n): 
    for j in range(i,n):
        print("*", end=' ')
        
    for j in range(i):
        print(" ", end=' ')
        
    for j in range(i):
        print(" ", end=' ')
    for j in range(i,n):
        print("*", end=' ')
    print()    

*                 * 
* *             * *
* * *         * * *
* * * *     * * * * 
* * * * * * * * * *
* * * *     * * * * 
* * *         * * *
* *             * * 
*                 *

------------------------------------------------------------------------


n=5
p=1
for i in range(n):
    for j in range(i+1):
        print(p ,end=' ')#or i+1 in place of p
    p+=1
    print()    

1 
2 2
3 3 3
4 4 4 4
5 5 5 5 5
--------------------------------------------------------------

n=5
p=n
for i in range(n):
    for j in range(i+1):
        print(p ,end=' ')#or n-i in place of p
    p-=1
    print()  
5 
4 4
3 3 3
2 2 2 2
1 1 1 1 1
------------------------------------------------------------------
    
n=5
for i in range(n):
    p=1
    for j in range(i+1):
        print(p ,end=' ')#or j+1 in place of p
        p+=1
    print()

1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5
---------------------------------------------------------------------


#floyd triangle
n=4
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end=' ')
        p+=1
    print() 

1 
2 3
4 5 6
7 8 9 10
-----------------------------------------------------------------------       

n=5
for i in range(n):
    for j in range(n):
        if(j==0 or j==n-1):
            print(" * ",end=' ')
        else:
            print(" ",end=' ')    
    print();    

 *         *  
 *         *
 *         *
 *         *  
 *         *
--------------------------------------------------------------------------

n=5
for i in range(n):
    for j in range(n):
        if(j==n//2 or i==n//2):
            print("*",end=' ')
        else:
            print(" ",end=' ')    
    print(); 

    *     
    *
* * * * *
    *
    *

--------------------------------------------------------------------------

n=5
for i in range(n):
    for j in range(n):
        if(i==j or i+j==n-1):
            print("*",end=' ')
        else:
            print(" ",end=' ')    
    print(); 

*       * 
  *   *
    *
  *   *
*       *
---------------------------------------------------------------------------
n=5
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==n-1 or j==n-1):
            print("*",end=' ')
        else:
            print(" ",end=' ')    
    print()

* * * * * 
*       *
*       *
*       *
* * * * *    
-------------------------------------------------------------------------

n=5
for i in range(n):
    for j in range(i+1):
        if(j==0 or i==n-1 or i==j):
            print("*",end=' ')
        else:
            print(" ",end=' ')    
    print()    
* 
* *
*   *
*     *
* * * * *
-------------------------------------------------------------------------

n=5
for i in range (n):
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i):
        if (j==0 or i==n-1):
            print("*",end=' ')
        else:
            print(" ",end=' ')    
    for j in range(i+1):
        if (j==i or i==n-1):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()     

          * 
        *   *
      *       *
    *           *
  * * * * * * * * *
-----------------------------------------------------------------------

n=5
for i in range(n-1):
    for j in range(i,n-1):
        print(" ",end=' ')
    for j in range(i):
        if (j==0):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    for j in range(i+1):
        if (i==j):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()    
for i in range(n):
    for j in range(i):
        print(" ",end=' ')
    for j in range(i,n):
        if (i==j):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    for j in range(i,n-1):
        if (j==n-2):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()                
        *
      *   *
    *       *
  *           *
*               *
  *           *
    *       *
      *   *
        *
------------------------------------------------------------------
'''    
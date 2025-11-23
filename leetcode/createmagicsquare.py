#It generates an odd-order Magic Square using the Siamese method (also called the "De la Loubère method").

# A magic square is a grid where:

# Numbers from 1 to n² are placed

# Every row, column, and diagonal has the same sum
# The Siamese method works as follows:
#UP RIGHT ....if occupied go DOWN instead
class MagicSquare:
    def generate(self,n):
        if n %2 == 0 or n<3:
            raise ValueError("only odd 3 <")
        magic=[[0]*n for _ in range(n)]
        i,j = 0 , n//2
        for num in range(1,n*n+1):
            magic[i][j]=num
            new_i=(i-1)%n #UP
            new_j=(j+1)%n #RIGHT
            if magic[new_i][new_j]!=0:
                i=(i+1)%n
            else:
                i,j=new_i,new_j
        return magic            

if __name__ == "__main__":
    n = 3
    ms = MagicSquare()
    square = ms.generate(n)
    for row in square:
        print(row)

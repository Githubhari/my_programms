"""The Following problem may be a normal problem but it is solved in O(n) using different technique from GFG"""

def transpose(self,matrix, n):
        for i in range(n):
            row1=i+1
            col1=i+1
            row0=0
            col0=0
            while row1<n and col1<n:
                matrix[row1][col0],matrix[row0][col1]=matrix[row0][col1],matrix[row1][col0]
                row1+=1
                col0+=1
                col1+=1
                row0+=1
             

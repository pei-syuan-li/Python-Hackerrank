
def surfaceArea(A): 
    n_rows = len(A) 
    n_cols = len(A[0]) 
    area = n_rows*n_cols*2 
    for i in range(n_rows): 
       for j in range(n_cols):
          val = A[i][j] 
          if i == 0 : 
              pre_row_val = 0 
          else: 
              pre_row_val = A[i-1][j]
          area += abs( val - pre_row_val )
          if i == n_rows-1:  
              area += val
          if j==0 : 
              pre_col_val = 0 
          else: 
              pre_col_val = A[i][j-1]          
          area += abs( val - pre_col_val ) 
          if j == n_cols-1: 
              area += val 
    return area

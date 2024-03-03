def solving(A):
# getting number of boxes
    N = len(A)
    #  target number of bricks in each box
    min_bricks = 10
     # Initialize the total number of moves
    total_moves = 0
    # iterate through the boxes
    for i in range(N - 1, 0, -1):
         # Calculate the difference between the bricks in the current box and the target
        deficit = A[i] - min_bricks
         # Add the absolute value of the difference to the total moves
        total_moves += abs(deficit)
        # Update the number of bricks in the box to the target
        A[i - 1] += deficit
    
    if A[0] == min_bricks:
        return total_moves
    else:
        return -1
# test case
print(solving([11, 10, 8, 12, 8, 10, 11]))  
print(solving([7, 14, 10])) 

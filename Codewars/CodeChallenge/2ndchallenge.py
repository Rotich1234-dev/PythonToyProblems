def max_sum_of_digits(n):
    # Function to calculate the sum of digits of a number
    return sum(map(int, str(n)))

def function_solution(A):
    # Dictionary to store numbers with the same digit sum
    add_integers = {}  
    max_sum = -1 
     # Initialize the maximum sum
    
    for num in A:
        sum_total = max_sum_of_digits(num)
        
        # Calculate the sum with the current number and the one stored in the dictionary
        current_pair_sum = num + add_integers.get(sum_total, 0)
        
       
        max_sum = max(max_sum, current_pair_sum)
        
        # Store the maximum of the current number and the one stored in the dictionary
        add_integers[sum_total] = max(add_integers.get(sum_total, 0), num)
    
    return max_sum

# Test cases

print(function_solution([42, 33, 60]))  
print(function_solution([51, 32, 43]))  

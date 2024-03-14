def max_sum_of_digits(n):
    # Function to calculate the sum of digits of a number
    return sum(map(int, str(n)))

def function_solution(A):
    # Dictionary to store numbers with the same digit sum
    add_integers = {}  
    max_sum = -1 
    # Initialize the maximum sum
    
    # List to store unique digit sums
    unique_sums = set()
    
    for num in A:
        sum_total = max_sum_of_digits(num)
        
        # Add the digit sum to the set of unique sums
        unique_sums.add(sum_total)
        
        # Calculate the sum with the current number and the one stored in the dictionary
        current_pair_sum = num + add_integers.get(sum_total, 0)
        
        # Update the maximum sum
        max_sum = max(max_sum, current_pair_sum)
        
        # Store the maximum of the current number and the one stored in the dictionary
        add_integers[sum_total] = max(add_integers.get(sum_total, 0), num)
    
    # If all numbers have distinct digit sums, return -1
    if len(unique_sums) == len(A):
        return -1
    
    return max_sum

# Test cases
print(function_solution([42, 33, 60]))  
print(function_solution([51, 71, 17, 42]))  
print(function_solution([51, 32, 43]))  

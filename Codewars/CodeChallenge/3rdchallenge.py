def answer(N):
    total_alphabet = "abcdefghijklmnopqrstuvwxyz"
    complete_set = N // 26
    remaining_chars = N % 26

    # Create the repeated pattern of the alphabet for full sets
    pattern = total_alphabet * complete_set

    # Add the remaining characters to the pattern
    pattern += total_alphabet[:remaining_chars]

    return pattern

# Test cases
print(answer(3))
print(answer(30))

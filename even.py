# Program to count even and odd numbers in a list

# Take list of numbers from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Initialize counters
even_count = 0
odd_count = 0

# Loop through numbers
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Display results
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)

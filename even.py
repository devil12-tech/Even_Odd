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

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Take list of numbers from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Count primes
prime_count = 0
for num in numbers:
    if is_prime(num):
        prime_count += 1

# Display result
print("Prime numbers count:", prime_count)

# Display results
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)

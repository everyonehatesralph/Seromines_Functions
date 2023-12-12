def smallest_factor(num):
    if num < 2:
        return "Cannot factor a number less than 1."

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return i
    return num


print('Finding the Smallest Factor')
number = int(input("Enter a number: ").strip())

result = smallest_factor(number)
print(f"The smallest factor of {number} is {result}\n")


def generate_primes_in_range(start, end):
    primes = []

    for num in range(max(2, start), end + 1):
        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return primes


# Example usage
print('Finding the Prime Numbers between the two numbers.')
start_range = int(input("Enter the start of the range: ").strip())
end_range = int(input("Enter the end of the range: ").strip())
prime_numbers = generate_primes_in_range(start_range, end_range)

print(f"The Prime numbers between {start_range} and {end_range} is: \n{prime_numbers}")
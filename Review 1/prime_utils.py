def generate_numbers(n):
    return list(range(1, n+1))

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        return True
    return False

def get_primes(nums):
    return list(filter(lambda x: is_prime(x), nums))

def square_primes(nums):

    primes = get_primes(nums)
    return list(map(lambda x: x * x, primes))

def squares(n):
    return n * n

if __name__ == "__main__":

    n = int(input("Enter number : "))
    nums = generate_numbers(n)
    primes = get_primes(nums)
    square = square_primes(nums)

    print(f"Primes: {primes}")
    print(f"Squares: {square}")

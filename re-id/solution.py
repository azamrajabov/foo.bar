def solution(i):
    primes_str = '2'
    n = 1
    while len(primes_str) <= (i+5):
        # even numbers can't be prime, skipping even numbers
        n += 2
        primes_str += get_prime_number(n)
    return primes_str[i:i+5]

def get_prime_number(n):
    prime_str = str(n)
    # try to devide till half of n
    for i in range(2, n//2 + 1):
        if n % i == 0:
            prime_str = ''
            break
    return prime_str


# print('the number:')
# x = input()
# print(solution(int(x)))

r = solution(0)
print(r)
assert r == '23571'

r = solution(3)
print(r)
assert r == '71113'

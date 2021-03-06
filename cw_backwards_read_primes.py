"""Codewars: Backwards Read Primes

6 kyu

URL:https://www.codewars.com/kata/5539fecef69c483c5a000015/train/python

Backwards Read Primes are primes that when read backwards in base 10 
(from right to left) are a different prime. (This rules out primes which 
are palindromes.)

Examples:
13 17 31 37 71 73 are Backwards Read Primes
13 is such because it's prime and read from right to left writes 31 
which is prime too. Same for the others.
Task
Find all Backwards Read Primes between two positive given numbers 
(both inclusive), the second one always being greater than or equal to 
the first one. The resulting array or the resulting string will be 
ordered following the natural order of the prime numbers.

Example
backwardsPrime(2, 100) => [13, 17, 31, 37, 71, 73, 79, 97]
backwardsPrime(9900, 10000) => [9923, 9931, 9941, 9967]
backwardsPrime(501, 599) => []

Note for Forth
Return only the first backwards-read prime between start and end or 0 if
you don't find any

backwardsPrime(2, 100) => [13, 17, 31, 37, 71, 73, 79, 97] 
backwardsPrime(9900, 10000) => [9923, 9931, 9941, 9967]
"""


# backwardsPrime is renamed backwards_prime
def backwards_prime(start, stop):
    lst = []
    if start < 4:
        start = 4
    while start < stop + 1:
        for i in range(2, int(start ** 0.5 + 1)):
            if start % i == 0:
                break
        if start % i != 0:
            lst.append(start)
        start += 1
    
    lst1 = []
    for i in lst:
        ii = str(i)[::-1]
        if int(ii) != i:
            lst1.append(int(ii))

    lst2 = []
    if stop <= 100:
        for i in lst1:
            if i > 11 and i in lst:
                i_i = str(i)[::-1]
                lst2.append(int(i_i))
        return lst2
    else:
        for i in lst1:
            for ii in range(2, int(i ** 0.5 + 1)):
                if i % ii == 0:
                    break
            if i % ii != 0:
                i_i = str(i)[::-1]
                lst2.append(int(i_i))
        return lst2


def main():
    # Output: [13, 17, 31, 37, 71, 73, 79, 97]
    start, stop = 2, 100
    print(backwards_prime(start, stop))

    # Output: [9923, 9931, 9941, 9967]
    start, stop = 9900, 10000
    print(backwards_prime(start, stop))

    # Output: []
    start, stop = 501, 599
    print(backwards_prime(start, stop))

    # Output: []
    start, stop = 400, 503
    print(backwards_prime(start, stop))

    # Output: [7027, 7043, 7057]
    start, stop = 7000, 7100
    print(backwards_prime(start, stop))


if __name__ == '__main__':
    main()


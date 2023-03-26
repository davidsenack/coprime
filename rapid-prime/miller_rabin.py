"""
 Copyright (C) 2023 David Senack
 
 This file is part of rapid-prime.
 
 rapid-prime is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 rapid-prime is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with rapid-prime.  If not, see <http://www.gnu.org/licenses/>.
"""

import random
import gmpy2


def miller_rabin_test(n, k=10):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    # Find r and d such that n = 2^r * d + 1
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Witness loop
    @par # <--- Codon compiler decorator
    for _ in range(k):
        a = gmpy2.mpz(random.randint(2, n - 2))
        x = gmpy2.powmod(a, d, n)
        if x == 1 or x == n - 1:
            continue
        @par # <--- Codon compiler decorator
        for _ in range(r - 1):
            x = gmpy2.powmod(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


'''
# Example usage
n = gmpy2.mpz('1000000000000037')  # Large prime number
is_prime = miller_rabin_test(n)
print(f"{n} is {'probably prime' if is_prime else 'not prime'}")
'''

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

def miller_rabin(n, k):

    '''
    Implementation uses the Miller-Rabin Primality Test
    The optimal number of rounds for this test is 40
    See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    for justification
    '''

    # Convert input number to n-bit integer for use with Codon
    width = len(n)
    n = Int[width](n)

    # Set up constants to corresponding n-bit width
    zero = Int[width](0)
    one = Int[width](1)
    two = Int[width](2)

    # If number is even, it's a composite number
    if n == two:
        return True
    if n % two == zero:
        return False

    # Set up variables for Miller-Rabin test
    r, s = zero, n - one
    while s % two == zero:
        r += one
        s //= two
    
    @par # <-- Parallelize this loop with Codon
    for _ in range(k):
        a = random.randrange(2, n - 1)
        a = Int[width](a) # Convert to n-bit integer
        x = pow(a, s, n)
        if x == one or x == n - one:
            continue
        
        @par # <-- Parallelize this loop with Codon
        for _ in range(r - one):
            x = pow(x, two, n)
            if x == n - one:
                break
        else:
            return False
    return True

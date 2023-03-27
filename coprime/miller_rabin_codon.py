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

from sys import argv
from random import SystemRandom as die # A single dice.
import time


def single_test(n, a):
    exp = n - 1
    while not exp & 1:
        exp >>= 1
        
    if pow(a, exp, n) == 1:
        return True
        
    while exp < n - 1:
        if pow(a, exp, n) == n - 1:
            return True
            
        exp <<= 1
        
    return False
    

def miller_rabin(n, k=10):
    for i in range(k):
        a = die.randrange(2, n - 1)
        if not single_test(n, a):
            return False
            
    return True


def mersenne_prime(n):
    return miller_rabin(2 ** n - 1)


def main():
    if len(argv) == 1:
        print("Usage: python3 miller_rabin.py [number]")
        return
    elif len(argv) == 2:
        n = int(argv[1])
        print(miller_rabin(n))
    elif len(argv) == 3:
        n = int(argv[1])
        k = int(argv[2])
        print(miller_rabin(n, k))
    else:
        print("Too many arguments.")
        return

if __name__ == "__main__":
    main()


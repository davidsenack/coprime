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

import argparse
import gmpy2

from miller_rabin import miller_rabin_test


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Test if a number is prime')
    parser.add_argument('number', type=int, help='Number to test')
    parser.add_argument(
        '-m', type=int, help='Specifies that the number is a Mersenne prime exponent (m in 2^m - 1)')
    parser.add_argument('-k', type=int, default=10,
                        help='Number of iterations. Seven iterations is generally considered sufficient')
    args = parser.parse_args()

    # If the user specified an exponent, calculate the number
    if args.m:
        args.number = 2 ** args.m - 1

    # Convert the number to a gmpy2 mpz object and test it
    candidate_num = gmpy2.mpz(args.number)
    is_prime = miller_rabin_test(candidate_num, args.k)

    # Print the result based on whether the user specified an exponent
    if args.m:
        print(f"M{args.m} is {'probably prime' if is_prime else 'not prime'}")
    else:
        print(f"{candidate_num} is {'probably prime' if is_prime else 'not prime'}")


if __name__ == '__main__':
    main()

# Path: rapid-prime/miller_rabin.py
# Compare this snippet from rapid-prime/miller_rabin.py:
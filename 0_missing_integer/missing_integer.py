#!/usr/bin/env python3
"""
Find the smallest positive integer that
does not occur in a given sequence
"""


def missing_integer(A):

    if A == []:
        return 1

    integers = []
    for i in A:
        if i >= 0:
            integers.append(i)

    maxi = max(A)

    if integers == []:
        return 1

    all_integers = []
    for i in range(1, maxi + 1):
        all_integers.append(i)

    missing = []
    for i in all_integers:
        if i not in integers:
            missing.append(i)

    return min(missing)


A = [1, 9, 8, 4, 5, 3, 2, -6]
# 6
print(missing_integer(A))

B = []
# 1
print(missing_integer(B))

C = [-2, -9, -3]
# 1
print(missing_integer(C))

#!/usr/bin/env python3
"""
Find the smallest positive integer that
does not occur in a given sequence
"""


def missing_integer(A):

    if A == []:
        return 1

    positive = []
    for i in A:
        if i > 0:
            positive.append(i)

    maxi = max(A)

    if positive == []:
        return 1

    all_positive = []
    for i in range(1, maxi + 1):
        all_positive.append(i)

    missing = []
    for i in all_positive:
        if i not in positive:
            missing.append(i)

    return min(missing)


A = [1, 9, 8, 4, 5, 3, 2, -6, 0]
# 6
print(missing_integer(A))

B = []
# 1
print(missing_integer(B))

C = [-2, -9, -3, 0]
# 1
print(missing_integer(C))

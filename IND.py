#!/usr/bin/ env python3
# -*- coding: utf-8 -*-

#Составить программу для решения задачи: В списке, состоящем из вещественных элементов, вычислить:1)
#максимальный по модулю элемент списка; 2) сумму элементов списка, расположенных между первым и вторым
#положительными элементами. Преобразовать список таким образом, чтобы элементы, равные нулю,
#располагались после всех остальных.

import sys

if __name__ == '__main__':
    A = list(map(int, input().split()))
    B = []
    for i in A:
        B.append(abs(i))
    m = max(B)
    t = []
    z = []
    for f in range(len(A)):
        if A[f] != 0:
            t.append(A[f])
        else:
            z.append(A[f])
    ip = (u for u, e in enumerate(A) if e > 0)
    print(t + z)
    print(sum(A[next(ip) + 1:next(ip)]))
    print(m)
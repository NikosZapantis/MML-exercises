import numpy as np
from math import gcd

#? 2.2.a Check if (Z_n, +) is abelian group

def is_abelian_group(n):
    elem = np.arange(n)
    id = 0

    # In each check I always use mod n
    # Checking closure for all a,b in Z_n
    closed = all(((a + b) % n) in elem for a in elem for b in elem)

    # Associativity: (a + b) _ c = a + (b + c)
    associative = all(((a + b) + c) % n == (a + (b + c)) % n for a in elem for b in elem for c in elem)

    # Id check: a + 0 = a
    id_ok = all(((a + id) % n == a) for a in elem)

    # Inverse check: for each a, there exists b such that a + b = 0
    inv_ok = all(any(((a + b) % n == id) for b in elem) for a in elem)

    # Commutativity: a + b = b + a
    com = all(((a + b) % n == (b + a) % n) for a in elem for b in elem)
    return closed and associative and id_ok and inv_ok and com

print("~ 2.2 (a) Abelian check ~")
print(is_abelian_group(5)) # Expected: True
print()

#? 2.2.b Multiplication at Z_n

def table_multiplication(n):
    elem = list(range(1, n))
    table = np.zeros((n-1, n-1), dtype=int)

    # Filling multiplication table: (i, j) = (a * b) % n
    for i, a in enumerate(elem):
        for j, b in enumerate(elem):
            table[i, j] = (a * b) % n
    return elem, table

els, tab = table_multiplication(5)
print("~  2.2 (b) Multiplication table in Z5 ~")
print("Elements:", els)
print(tab)
print()

#? 2.2.b Inverses

def find_inverses(n):
    inv = {}

    # For each elem a, I try to find b such that (a * b) % n = 1
    for a in range(1, n):
        for b in range(1, n):
            if (a * b) % n == 1:
                inv[a] = b
                break # If one inverse is found, stop
    return inv

print("~ 2.2 (b) Inverses in Z5 ~")
print("Inverses in Z5:", find_inverses(5))
print()

#? 2.2.c Check if Z8 is a group

def is_group(n):
    elem = list(range(1, n))

    #! Checking for closure
    for a in elem:
        for b in elem:
            if (a * b) % n not in elem:
                return False
    
    #! Checking for inverses [Using gcd (Great Common Divisor)]
    # Sources [https://stackoverflow.com/questions/11175131/code-for-greatest-common-divisor-in-python & https://www.geeksforgeeks.org/python/gcd-in-python/ ]
    for a in elem:
        if gcd(a, n) != 1:
            return False
    return True

print("~ 2.2 (c) Is Z8 a group? ~")
print("(Z5, x) group: ", is_group(5)) # Expected: True
print("(Z8, x) group: ", is_group(8)) # Expected: False
print() 

"""
55555
4444
333
22
1
"""

def patter_4(n):
    for i in range(n,0,-1):
        for j in range(i):
            print(i, end="")
        print()

patter_4(5)
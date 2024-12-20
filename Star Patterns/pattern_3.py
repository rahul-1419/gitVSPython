"""
55555
44444
33333
22222
11111
"""

def third_pattern(n):
    for i in range(n,0,-1):
        for j in range(n):
            print(i , end="")
        print()

third_pattern(5)

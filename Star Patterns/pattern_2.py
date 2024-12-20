"""
11111
22222
33333
44444
55555
"""

def sec_pattern(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i ,end="")
        print()

sec_pattern(5)

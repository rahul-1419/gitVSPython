"""
1
12
123
1234
12345
"""

def pattern_6(n):
    for i in range (1,n+1):
        for j in range(i):
            print(j+1,end="")
        print()

pattern_6(5)
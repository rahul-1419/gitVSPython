"""
5
54
543
5432
54321
""" 

def pattern_7(n):
    for i in range(1,n+1):
        for j in range(n,n-i,-1):
            print(j,end="")
        print()

pattern_7(5)
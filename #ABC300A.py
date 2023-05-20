#ABC300A
import sys

N,A,B = map(int,input().split())
C = list(map(int,input().split()))

for i, c in enumerate(C):
    #print(i,c)
    if c  == A+B:
        
        print(i+1)
        sys.exit()
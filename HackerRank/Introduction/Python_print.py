"""
Example:
n = 5
Print the string 12345.
"""

#Solution 1
print(*range(1, int(input()) + 1), sep="")  
#Solution 2
n = int(input())
print(''.join(map(str,range(1,n+1))))
#Solution 3
list(map(lambda x:print(x + 1, end=''), range(int(input()))))

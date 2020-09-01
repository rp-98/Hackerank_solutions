# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n=int(input())
task=[input().split(" ") for _ in range(n)]
d=deque()
for x in task:
    if x[0]=='append':
        d.append(int(x[1]))
    elif x[0]=='appendleft':
        d.appendleft(x[1])
    elif x[0]=='pop':
        d.pop()
    elif x[0]=='popleft':
        d.popleft()
print(*list(d))

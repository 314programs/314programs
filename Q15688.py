import sys
caseCount = int(sys.stdin.readline().rstrip())
CountList = [0]*2000001
for i in range(caseCount):
  CountList[int(sys.stdin.readline().rstrip())+1000000] += 1

for i in range(2000001):
  for a in range(CountList[i]):
    sys.stdout.write(str(i-1000000) + '\n')

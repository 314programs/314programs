import sys
CaseCount, MinNumber = map(int, sys.stdin.readline().split())
NumberList = list(map(int, sys.stdin.readline().split()))

Min = 1
Max = max(NumberList)

while Min <= Max:
  Total = 0
  Mid = (Min+Max)//2

  for item in NumberList:
    temp = item - Mid

    if temp > 0:
      Total += temp

  if Total < MinNumber:
    Max = Mid - 1
  else:
    Min = Mid + 1

print(Max)

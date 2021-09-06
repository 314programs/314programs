CaseCount = int(input())
for i in range(CaseCount):
  NumList = list(map(int, input().split()))
  NumList.sort()
  print(NumList[7])

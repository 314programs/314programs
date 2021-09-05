CaseCount = int(input())
NumList = []
for i in range(CaseCount):
  NumList.append(int(input()))

NumList.sort()

for item in NumList:
  print(item)

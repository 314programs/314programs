import sys
ListLength = int(sys.stdin.readline().rstrip())
NumList = list(map(int, sys.stdin.readline().rstrip().split()))
NumDict = {}

for i in NumList:
  if i in NumDict:
    NumDict[i] += 1
  else:
    NumDict[i] = 1

SortedNums = sorted(NumDict.items(), key = lambda x:x[0])
SortingDict = {}

for i in range(len(SortedNums)):
  SortingDict[SortedNums[i][0]] = i

ResultsList = []
for item in NumList:
  ResultsList.append(str(SortingDict[item]))

sys.stdout.write(' '.join(ResultsList))

ListLength = int(input())
TheList = list(map(int, input().split()))

TheList.sort()

Temp = 0
for i in range(ListLength):
  Temp += TheList[i]
  for x in range(i):
    Temp += TheList[x]
    
print(Temp)

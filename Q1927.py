import sys
import heapq
CaseCount = int(sys.stdin.readline().rstrip())
TheList = []
heapq.heapify(TheList)

for i in range(CaseCount):
  Word = int(sys.stdin.readline().rstrip())
  if Word == 0:
    if len(TheList) == 0:
      sys.stdout.write('0' + '\n')
    else:
      sys.stdout.write(str(heapq.heappop(TheList))+ '\n')
  
  else:
    heapq.heappush(TheList, Word)

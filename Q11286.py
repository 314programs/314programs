import heapq
import sys
CaseCount = int(sys.stdin.readline().rstrip())
TheList = []
heapq.heapify(TheList)

for i in range(CaseCount):
  Word = int(sys.stdin.readline().rstrip())
  if Word == 0:
    if len(TheList) == 0:
      sys.stdout.write('0'+'\n')
    else:
      sys.stdout.write(str(heapq.heappop(TheList)[1])+'\n')
  
  else:
    heapq.heappush(TheList, [abs(Word), Word])

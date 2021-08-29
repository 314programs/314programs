import sys
ItemNum, QuestionNum = map(int, sys.stdin.readline().rstrip().split())
Dictionary = {}
TheList = []
for i in range(ItemNum):
  Website, Password = map(str, sys.stdin.readline().rstrip().split())
  Dictionary[Website] = Password

for i in range(QuestionNum):
  TheWebsite = sys.stdin.readline().rstrip()
  TheList.append(Dictionary[TheWebsite])

for item in TheList:
  sys.stdout.write(item + '\n')

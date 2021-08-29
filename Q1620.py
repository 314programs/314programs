import sys

PokiNum, QuestionNum = map(int, sys.stdin.readline().split())
PokiListDict = {}
ReverseDict = {}
for i in range(PokiNum):
  Name = sys.stdin.readline().rstrip()
  PokiListDict[i+1] = Name
  ReverseDict[Name] = i+1

for i in range(QuestionNum):
  Question = sys.stdin.readline().rstrip()
  try:
    int(Question)
    sys.stdout.write(PokiListDict[int(Question)] + '\n')
  except ValueError:
    sys.stdout.write(str(ReverseDict[Question]) + '\n')

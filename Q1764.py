PeopleNum, QuestionNum = map(int, input().split())
PeopleDict = {}
QuestionList = []
for i in range(PeopleNum):
  PeopleDict[input()] = 1

for i in range(QuestionNum):
  Question = input()
  if Question in PeopleDict:
    QuestionList.append(Question)

print(len(QuestionList))
QuestionList.sort()
for item in QuestionList:
  print(item)

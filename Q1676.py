Number = int(input())
Total = 1
Streak = 0
StreakList = []

for i in range(Number, 0, -1):
  Total *= i

Total = str(Total)

for char in Total[::-1]:
  if char == '0':
    Streak += 1
  else:
    Streak = 0

  StreakList.append(Streak)

print(max(StreakList))

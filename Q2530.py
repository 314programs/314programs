import math
Hours, Minutes, Seconds = map(int, input().split())
AddSec = int(input())

TotalSec = Seconds + AddSec
PrintSeconds = TotalSec%60

TotalMin = math.floor(TotalSec//60) + Minutes
PrintMinutes = TotalMin%60

PrintHours = (Hours + math.floor(TotalMin//60))%24

print(str(PrintHours) + ' ' + str(PrintMinutes) + ' ' + str(PrintSeconds))

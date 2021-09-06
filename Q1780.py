import sys

Dimension = int(sys.stdin.readline().rstrip())
ListMap = []
for i in range(Dimension):
  ListMap.append(list(map(int, sys.stdin.readline().rstrip().split())))
Dictionary = {-1:0, 0:0, 1:0}

def TheDivision(Dimension, CheckList):
  Division = Dimension//3
  #Count and if there was count, return
  if Division > 0:
    for i in range(-1,2):
      if CheckList.count([i]*Dimension) == Dimension:
        Dictionary[i] += 1
        return
        
    #Divide into 9 sections if there was no count
    for y in range(0, Dimension, Division):
      for x in range(0, Dimension, Division):
        Temp = []
        for r in range(y, y+Division):
          Temp.append(CheckList[r][x:x+Division])
        TheDivision(Division, Temp)        
    
  else:
    for i in range(-1,2):
      Dictionary[i] += CheckList.count([i])
    return


TheDivision(Dimension, ListMap)
sys.stdout.write(str(Dictionary[-1]) + '\n')
sys.stdout.write(str(Dictionary[0]) + '\n')
sys.stdout.write(str(Dictionary[1]) + '\n')

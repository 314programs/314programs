Dimension = int(input())
Dictionary = {1:0, 0:0}
ListMap = []
for i in range(Dimension):
  ListMap.append(list(map(int, input().split())))

def DimensionDivision(TheDimension, DimensionList, TheDict):

    if DimensionList.count([1]*(TheDimension)) == TheDimension:
      Dictionary[1] += 1
    elif DimensionList.count([0]*(TheDimension)) == TheDimension:
      Dictionary[0] += 1

    else:
      SectionOne = []
      for i in range(TheDimension//2):
        SectionOne.append(DimensionList[i][0:TheDimension//2])

      SectionTwo = []
      for i in range(TheDimension//2):
        SectionTwo.append(DimensionList[i][TheDimension//2: TheDimension])

      SectionThree = []
      for i in range(TheDimension//2):
        SectionThree.append(DimensionList[i+TheDimension//2][0:TheDimension//2])

      SectionFour = []
      for i in range(TheDimension//2):
        SectionFour.append(DimensionList[i+TheDimension//2][TheDimension//2: TheDimension])


      AllSection = [SectionOne, SectionTwo, SectionThree, SectionFour]
      for item in AllSection:
        DimensionDivision(TheDimension//2, item, TheDict)

DimensionDivision(Dimension, ListMap, Dictionary)
print(str(Dictionary[0]))
print(str(Dictionary[1]))

def PrimeCheck(number):
  Divisible1 = 0
  for i in range(1,number + 1):
    if (number/i).is_integer():
      Divisible1 = Divisible1 + 1
  
  if Divisible1 <= 2:
    return True
  else:
    return False

primeList = []

for i in range (1, 1000):
  if PrimeCheck(i) == True:
    primeList.append(i)

print(primeList)

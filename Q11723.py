import sys
S = 0b0
IterCount = int(sys.stdin.readline().rstrip())
for i in range(IterCount):
  Question = sys.stdin.readline().rstrip()
  if 'all' == Question:
    S = (1<<20)-1
  elif 'empty' == Question:
    S = 0
  else:
    if 'add ' in Question:
      CleanQuestion = Question.replace('add ', '')
      S |= (1<<int(CleanQuestion)-1)
    
    elif 'remove ' in Question:
      CleanQuestion = Question.replace('remove ', '')
      S &= ~(1<<int(CleanQuestion)-1)
    
    elif 'check ' in Question:
      CleanQuestion = Question.replace('check ', '')
      if S & (1 << int(CleanQuestion)-1) == 0:
        sys.stdout.write('0' + '\n')
      else:
        sys.stdout.write('1' + '\n')
    elif 'toggle ' in Question:
      CleanQuestion = Question.replace('toggle ', '')
      S ^= (1 << int(CleanQuestion)-1)

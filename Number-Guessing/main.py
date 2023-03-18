import sys
t = int(input())

for i in range(t):

  a, b = map(int, input().split())
  n = int(input())

  for j in range(n):
    
    p = (a + b) // 2
    print(p)
    sys.stdout.flush()
    decision = input()
    
    if (decision == "TOO_BIG"):
  
      b = p - 1
    elif (decision == "TOO_SMALL"):
  
      a = p + 1
    elif (decision == "CORRECT"):
  
      break
    elif (decision == "WRONG_ANSWER"):
  
      break
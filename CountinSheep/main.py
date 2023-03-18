import sys
t = int(input())

for i in range(t):

  n = input()
  arr = [int(a) for a in n]
  k = 1
  while (True):

    if (int(n) == 0):
  
      print(f"Case #{i + 1}: INSOMNIA")
      sys.stdout.flush
      break
    else:
      
      passedCases = 0
      for j in range(0, 10):
    
        if (j in arr):
    
          passedCases += 1
        else:
    
          m = str(int(n) * k)
          break
  
      if(passedCases == 10):
    
        print(f"Case #{i + 1}: {m}")
        sys.stdout.flush()
        break
  
      k += 1
      arr.extend([int(a) for a in m])
      arr = list(dict.fromkeys(arr))
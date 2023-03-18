import sys
t = int(input())

for i in range(t):

  n = int(input())
  array = list(map(int, input().split()))
  
  cost = 0
  for j in range(n - 1):

    temp = array.copy()
    index_of_miniumum = array.index(min(array[j:]))

    index = 0
    for k in range(index_of_miniumum, j - 1, -1):

      array[j + index] = temp[k]     
      index += 1
    
    cost += index_of_miniumum - j + 1
  
  print(f"Case #{i + 1}: {cost}")
  sys.stdout.flush()
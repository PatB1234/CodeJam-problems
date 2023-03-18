import sys
t = int(input())

for p in range(t):

  r, c = map(int, input().split())

  pattern = []
  pattern.append(f"..{'+-' * (c - 1)}+")
  pattern.append(f"..{'|.' * (c - 1)}|")
  for i in range(r - 1):

    pattern.append(f"{'+-' * c}+")
    pattern.append(f"{'|.' * c}|")

  pattern.append(f"{'+-' * c}+")
  
  print(f"Case #{p + 1}:")
  sys.stdout.flush()
  for i in range(len(pattern)):

    print(pattern[i])
    sys.stdout.flush()
    
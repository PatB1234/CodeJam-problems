'''import sys
t = int(input())

for i in range(t):

  n = int(input())
  a = 1
  b = n
  tidy_a = int("".join(sorted([i for i in str(a)])))
  tidy_b = int("".join(sorted([i for i in str(b)])))
  while b != tidy_b:
    

    if (a == tidy_a):

      a = (a + b) // 2
    else:

      a = (1 + a) // 2
    
    b -= 1
    tidy_b = int("".join(sorted([i for i in str(b)])))
    
  print(f"Case #{i+1}: {b}")
  sys.stdout.flush()

'''

def tidy_numbers():
    digits = map(int, list(raw_input().strip()))
    for i in reversed(xrange(1, len(digits))):
        if digits[i] == 0 or digits[i] < digits[i-1]:
            for j in xrange(i, len(digits)):
                digits[j] = 9
            for j in reversed(xrange(i)):
                if digits[j] != 0:
                     digits[j] -= 1
                     break
                else:
                    digits[j] = 9
    return int("".join(map(str, digits)))

for case in xrange(input()):
    print('Case #%d: %s' % (case+1, tidy_numbers()))
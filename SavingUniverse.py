t = int(input())

def calcDamage(arr):

    damageTaken = 0
    beam = 1
    for j in range(len(arr)):

        if (arr[j] == 'C'):

            beam *= 2
        elif (arr[j] == 'S'):
            
            damageTaken += beam

    return damageTaken
        
def swap(c, pos1, pos2):

    arr = c
    p1 = pos1
    p2 = pos2
    temp = arr[p1]
    c[p1] = arr[pos2]
    c[p2] = temp
    
    return arr

def countS(c):

    j = 0
    for i in range(len(c)):

        if (c[i] == "S"):
            
            j += 1

    return j 


for i in range(t):

    string = input()
    string = string.split(" ")
    d = int(string[0])
    s = string[1]
    c = [a for a in s]
    swaps = 0


    
    damage = calcDamage(c)
    if (damage <= d):

        swaps = 0

    elif (countS(c) > d):

        swaps = "IMPOSSIBLE"
    else: 
        while (d < damage):
            if ("CS" in s):

                for j in range(-1, -len(c), -1 ):

                    if (c[j] == "S" and c[j-1] == "C" and d < damage):

                        c = swap(c, j - 1, j)
                        swaps += 1
                        damage = calcDamage(c)
                        break

            else:

                break

            damage = calcDamage(c)
    
    if (damage > d):

        swaps = "IMPOSSIBLE"

    print(f"Case #{i + 1}: {swaps}")

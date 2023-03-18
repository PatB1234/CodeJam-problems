array = []

for i in range(int(input("Enter how many numbers you want: "))):

  array.append(int(input("Enter a number: ")))

array = array.sort()

for j in range(len(array)):

  if (array[j] + 1 != array[j + 1]):

    print("The missing number is: ", array[j] + 1)
    break
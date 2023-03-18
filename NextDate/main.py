'''year = int(input('Input a year: '))
month = int(input('Input a month 1-12: '))
day = int(input('Input a day 1-31: '))

day += 1

if (month == 2):

  if (day > 28):

    month += 1
    day = 1

elif (month % 2 == 0):

  if (day > 30):
    
    month += 1
    day = 1
elif (month % 2 != 0):

  if (day > 31):

    month += 1
    day = 1


if (month > 12):

  year += 1
  month = 1
  day = 1

print("The next date is [yyyy-mm-dd] ", year, "-", month, "-", day)

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for i in range(len(list1)):

  if (list1[i] > 150):

    break
  elif (list1[i] % 5 == 0):

    print(list1[i])'''


Password= input('Please make a password wich contains 1 letter 1 special charecter and 1 integer lenght 6 and max lenght 16')
lenght=(len(Password))
alphabet=Password.isalpha()
upercase=Password.isupper()

FirV=False
SecV=False
ThrV=False
FouV=False
FivV=False



if lenght <= 16 and lenght >= 6:
  FirV=FirV=True


for a in Password:
    if a.isupper() == True:
        SecV=Secv=True    

for b in Password:    
    if b.islower() == True:
      ThrV=ThrV=True
    
for c in Password:    
    if '!' in c or '@' in c or '#' in c or '$' in c :
        FouV=FouV=True
    
for c in Password:    
    if '1' in c or '2' in c or '3' in c or '4' in c or '5' in c or '6' in c or '7' in c or '8' in c or '9' in c or '0' in c :
        FivV=FivV=True

if FirV==True:
  if SecV==True:
    if ThrV==True:
      if FouV==True:
        if FivV==True:
          print('You have succsessfuly created the password')
        else:
          print('your password needs to contain atleast 1 numerical charecter')
      else:
        print('your password needs to contain 1 special charecter')
    else:
      print('Your password need to contain 1 lowercase charecter')
  else:
    print('Your password needs to contain 1 upercase charecter')
else:
  print('Your password needs to be 6 to 16 digits')
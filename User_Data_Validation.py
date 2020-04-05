import random
import string

def randomString(stringLength=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def first2(s):
    return s[:2]

def last2(s):
    return s[-2:]

def createPassword():
    enterpassword = input("Enter a password of your choice :")
    while len(enterpassword) < 7:
        print("Password must be greater than or equal to 7 character")
        enterpassword = input("Enter a password of your choice :")
    return enterpassword
        
def choices():
    choice = input().capitalize()
    return choice
container = []
myDetails = []

def myDetailslist(s):
    for s in lists:
        print(lists)

def users():
    print('Enter your first name')
    firstname = input()
    myDetails.append(firstname)
    print('Enter your Last name')
    lastname = input()
    myDetails.append(lastname)
    print('Enter your email')
    email = input()
    myDetails.append(email)
    password = first2(firstname) + last2(lastname) + randomString()
    print("Are you satisfied with this password ", password,"Y/N")
    choice = input().capitalize()
    if choice == "N":
        nPassword = createPassword()
        myDetails.append(nPassword)
    elif choice == "Y":
        myDetails.append(password)
        #print(myDetails)
    else:
        print( "wrong input")

while True:
    users()
    for i in range(0, len(myDetails), 4):
            print('First Name:',myDetails[i], 'Last Name:',myDetails[i+1], 'Email:',myDetails[i+2], 'Password:',myDetails[i+3])
    print('Press Y to continue and N to End')
    choice = input().capitalize()
    if choice == 'Y':
        continue
    elif choice == 'N':
        print('====Good Bye====')
        break
        exit
    else:
        print('wrong input')
        choices()


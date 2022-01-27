from random import *
from string import ascii_lowercase, ascii_uppercase

def special(output):
    specialChars = ['@','#','$','%','&','_','?']
    for i in range(4):
        output.append(specialChars[randint(0,6)])

def upperCase(output):
    upperCase = list(ascii_uppercase)
    for i in range(randint(2,6)):
       output.append(upperCase[randint(0,25)])

def numbers(output):
    nums = [0,1,2,3,4,5,6,7,8,9]
    for i in range(randint(4,7)):
        output.append(nums[randint(0,9)])

def lowerCase(output):
    lowerCase = list(ascii_lowercase)
    for i in range(24):
        output.append(lowerCase[randint(0,25)])

def createPasswd():
    passList = []
    for i in range(1):
        output = []
        special(output)
        upperCase(output)
        numbers(output)
        shuffle(output)
        lowerCase(output)
        for i in range(randint(1,9)):
            shuffle(output)
        lowerCase(output)
        for i in range(3):
            output[i],output[len(output)-(i+1)] = output[len(output)-(i+1)], output[i]
        lowerCase(output)
        output[23] = choice(ascii_lowercase)
        passList.append(output)
    return passList

mainList = createPasswd()
print('Wachtwoord: ', *createPasswd[0][:24], sep='')
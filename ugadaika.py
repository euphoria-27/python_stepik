# объявление функции
from random import *

print('Welcome! Try to guess a number')


def is_valid(num):
    if(1 <= int(num) <= 100):
        return True
    else:
        return False
        
def play_again():
    print('wanna go agane? y/n')
    text = input()
    if(text == 'y'):
        ugadaika()
    elif(text == 'n'):
        return
    else:
        print('incorrect answer')
        play_again()
        
def ugadaika():
    print('give upper limit')
    upper_limit = int(input())
    rand_num = randint(1, upper_limit)
    tries = 0
    while(True):
        num = input()
        if(not is_valid(num)):
            print('Give valid number')
            continue
        else:
            num = int(num)
            if(num == rand_num):
                print('Correct! total number of guesses =', tries)
                tries += 1
                play_again()
                break
            elif(num < rand_num):
                print('you guessed lower')
                tries += 1
                continue
            elif(num > rand_num):
                print('you guessed higher')
                tries += 1
                continue

ugadaika()                
print('thank you for playing')

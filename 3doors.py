import random
import math
import time

# Win counts and results
swincount = 0
cwincount = 0
sresult = '\nStay Results: \n\n'
cresult = '\nChange Results \n\n'

# Spaces
spaces = '-------------------------------'
# Greetings
print('Hello and welcome to the three door choosing simulation made by Vovencio!')
print('This simulation simulates the three door quiz.')
print(spaces)
print('If you want to simulate, write:"start" and press enter')
print('Otherwise, if you want more info, write "info"')
print('But if you want to exit, just type "exit"')
print(spaces)

son = 0
nof = 'test'

def choose2():
    print(spaces)
    print('After completing, save the results to a file? (y/n/c) ')
    b = input('y = save, n = do not save, c = compromised ')
    if b == 'y':
        return 1
    elif b == 'n':
        return 0
    elif b == 'c':
        return 2
    else:
        print(spaces)
        print('Please answer with "y", "n" or "c"')
        print('y = save, n = do not save, c = compromised')
        choose2()
def choose():
    a = input('What are we going to do next, capitan? ')
    if a == 'info':
        print(spaces)
        print('The three door Quiz is a quiz show, you were invited to.')
        print('In front of you are three identical doors but only behind')
        print('one of them lie $1000000.')
        print('')
        print('You choose one of the doors without opening, after which the showmaster')
        print('opens another door, which has nothing behind it.')
        print('Now there are only 2 doors to choose from,')
        print('will you change your door or stay?')
        print(spaces)
        choose()
    elif a == 'exit':
        exit(0)
    elif a == 'start':
        return()
    else:
        print(spaces)
        print('Incorrect answer, repeat')
        print(spaces)
        choose()
choose()


# Count of tests to do
print(spaces)
print('Before starting to simulate, please answer a few questions for setup.')
count = int(input('Please provide a number of simulations which is greater than 0: '))
def ns():
    print(spaces)
    print('Error! The count number is too low!')
    l = int(input('Please provide a number of simulations which is GREATER than 0: '))
    if l < 1:
        ns()
    else:
        return l
if count < 1:
    count= ns()
print(spaces)
print('Warning! The simulation is all about chance,')
print('the more simulations you run the more correct the answers get.')
son = choose2()
if son == 1 or son ==2:
    print(spaces)
    nof = input('How to name the file? ')
print(spaces)
input('Starting the simulation, press Enter ')

# Time measurment
starttime = time.time()
rem = 0

for x in range(0,count):

    cur = time.time()
    if x % 10 == 0 and x !=0:
        rem = ((cur - starttime) * (count / x)) - (cur - starttime)
    hours = math.floor(rem / 3600)
    minutes = math.floor(((rem / 3600) - hours)*60)
    secs = math.floor(((((rem / 3600) - hours)*60-minutes)*60)*100)/100
    perc = math.floor(x/count*100000)/1000
    if x % 5 == 0:
        print('%s '%perc +"%" +' completed, estimated time: %s hours' %hours + ', minutes %s' %minutes + ', seconds %s' %secs)

    doors = [0,0,0]
    first = random.randint(0,2)
    doors[first] = 1
    selected = random.randint(0,2)
    if son ==1:
        sresult = sresult + '\nTest %s,' %x + 'treasure %s,' %first + 'selected/opened %s, ' %selected

    if doors[selected] == 1:
        swincount +=1
        sresult = sresult + 'won'
    else:
        sresult = sresult + 'lost'

    doors = [0,0,0]

    first = random.randint(0,2)
    doors[first] = 1
    selected = random.randint(0,2)
    if son ==1:
        cresult = cresult + '\nTest %s,' % x + 'treasure %s,' % first + 'selected %s, ' % selected
    if doors[selected] == 0:
        cwincount +=1
        if son == 1:
            cresult = cresult + 'won'
    else:
        if son == 1:
            cresult = cresult + 'lost'
dotime = math.floor((time.time()-starttime)*100)/100
print(spaces)
print(spaces)
print(spaces)
print(spaces)
print('Complete in %s seconds!' %dotime)
print(spaces)
print('If you stayed, you would have %s wins out of the total ' %swincount + '%s tries' %count)
swinperc = math.floor(swincount/count*10000)/100
print('Which is %s' %swinperc + '% win chance!')
print(spaces)
print('If you changed the door, you would have %s wins out of the total ' %cwincount + '%s tries' %count)
cwinperc = math.floor(cwincount/count*10000)/100
print('Which is %s' %cwinperc + '% win chance!')

if son != 0:
    ss = spaces + '\n'
    towrite = ss + 'Complete in %s seconds!\n' %dotime + ss + 'If you stayed, you would have %s wins out of the total ' %swincount + '%s tries \n' %count + ss + 'Which is %s' %swinperc + '% win chance! \n' + ss + 'If you changed the door, you would have %s wins out of the total ' %cwincount + '%s tries \n' %count + ss + 'Which is %s' %cwinperc + '% win chance!\n'

    file = open(nof +'.txt', "a")
    if son == 2:
        file.write(towrite)
    if son == 1:
        file.write(towrite + '\n\n\n\n' + sresult + '\n\n\n\n' + cresult)
input('Exit ')
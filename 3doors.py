import random
from multiprocessing import Process
import math
import time
if __name__ == '__main__':
    # Win counts and results
    swincount = 0
    cwincount = 0
    sresult = ['\nStay Results: \n\n']
    cresult = ['\nChange Results \n\n']

    # Spaces
    spaces = '-------------------------------'
    # Greetings
    print('Hello and welcome to the Monty Hall simulation made by Vovencio!')
    print('This simulation simulates the Monty Hall problem.')
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
            print('The Monty Hall is a quiz show, you were invited to.')
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

    print(spaces)
    for x in range(0,count):
        perc = math.floor(x/count*100000)/1000
        print("%s" %perc + "%" + ' Preparing' + '.'*(x%3+1))
        sresult.append('')
        cresult.append('')

def Rechnen(nm,nm2,tr):
    global cwincount
    global swincount
    global rem
    lead = 0
    for x in range(nm,nm2):
        if tr ==lead:
            cur = time.time()
            if x % 10 == 0 and x !=0:
                rem = (((cur - starttime) * (count / x)) - (cur - starttime))/12
            hours = math.floor(rem / 3600)
            minutes = math.floor(((rem / 3600) - hours)*60)
            secs = math.floor(((((rem / 3600) - hours)*60-minutes)*60)*100)/100

            perc = math.floor(x/count*100000*12)/1000
            if x % 5 == 0:
                print('%s'%perc +"%" +' completed, estimated time: %s hours' %hours + ', minutes %s' %minutes + ', seconds %s' %secs)

        doors = [0,0,0]
        first = random.randint(0,2)
        doors[first] = 1
        selected = random.randint(0,2)

        if doors[selected] == 1:
            swincount +=1
            if son == 1:
                sresult[x+1] =('\nTest %s,' % x + 'treasure %s,' % first + 'selected/opened %s, ' % selected + 'won')
        else:
            if son == 1:
                sresult[x+1] =('\nTest %s,' % x + 'treasure %s,' % first + 'selected/opened %s, ' % selected + 'lost')

        doors = [0,0,0]

        first = random.randint(0,2)
        doors[first] = 1
        selected = random.randint(0,2)
        if doors[selected] == 0:
            cwincount +=1
            if son == 1:
                cresult[x + 1]=('\nTest %s,' % x + 'treasure %s,' % first + 'selected %s, ' % selected + 'won')
        else:
            if son == 1:
                cresult[x + 1]=('\nTest %s,' % x + 'treasure %s,' % first + 'selected %s, ' % selected + 'lost')
    if tr == lead:
        print(spaces)
        print('Stand by...')
        print(spaces)
        lead +=1
if __name__ == '__main__':
    p0 = Process(target=Rechnen(0,math.floor(count/12),0), args=(0,0,0,))
    p1 = Process(target=Rechnen(math.floor(count/12),math.floor(count/12)*2,1), args=(0,0,0,))
    p2 = Process(target=Rechnen(math.floor(count/12)*2,math.floor(count/12)*3,2), args=(0,0,0,))
    p3 = Process(target=Rechnen(math.floor(count/12)*3,math.floor(count/12)*4,3), args=(0,0,0,))
    p4 = Process(target=Rechnen(math.floor(count/12)*4,math.floor(count/12)*5,4), args=(0,0,0,))
    p5 = Process(target=Rechnen(math.floor(count/12)*5,math.floor(count/12)*6,5), args=(0,0,0,))
    p6 = Process(target=Rechnen(math.floor(count/12)*6,math.floor(count/12)*7,6), args=(0,0,0,))
    p7 = Process(target=Rechnen(math.floor(count/12)*7,math.floor(count/12)*8,7), args=(0,0,0,))
    p8 = Process(target=Rechnen(math.floor(count/12)*8,math.floor(count/12)*9,8), args=(0,0,0,))
    p9 = Process(target=Rechnen(math.floor(count/12)*9,math.floor(count/12)*10,9), args=(0,0,0,))
    p10 = Process(target=Rechnen(math.floor(count/12)*10,math.floor(count/12)*11,10), args=(0,0,0,))
    p11 = Process(target=Rechnen(math.floor(count/12)*11,count,11), args=(0,0,0,))
    p0.start()
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
    p11.start()
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

    print(spaces)

    if son != 0:
        ss = spaces + '\n'
        towrite = ss + 'Complete in %s seconds!\n' %dotime + ss + 'If you stayed, you would have %s wins out of the total ' %swincount + '%s tries \n' %count + ss + 'Which is %s' %swinperc + '% win chance! \n' + ss + 'If you changed the door, you would have %s wins out of the total ' %cwincount + '%s tries \n' %count + ss + 'Which is %s' %cwinperc + '% win chance!\n'

        file = open(nof +'.txt', "a")
        if son == 2:
            file.write(towrite)
        if son == 1:
            savingperc = 0
            sstr = ''
            cstr = ''
            for x in range(0,len(sresult)):
                sstr = sstr +sresult[x]
                if x % 10 == 0:
                    savingperc = math.floor(x/(count*2+2) *10000)/100
                    print('Saving... %s' %savingperc + '%')
            for x in range(0,len(cresult)):
                cstr = cstr +cresult[x]
                if x % 10 == 0:
                    savingperc = math.floor(x/(count+1) *10000/100)/2+50
                    print('Saving... %s' %savingperc + '%')
            file.write(towrite + '\n\n\n\n\n' + sstr + '\n\n\n\n\n' + cstr)
    input('Exit ')
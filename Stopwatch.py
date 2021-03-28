import os
import time
second = 0
minute = 0
hours = 0
startfunc = input("To Start type Y\n")
if startfunc == 'Y':
    while(True):
        print("Simple stopwatch -----> @C0ders")
        print("\n\n\n")
        print("\t\t\t\t-----------")
        print("\t\t\t\t %d : %d : %d" %(hours, minute, second))
        print("\t\t\t\t-----------")
        time.sleep(1)
        second+=1
        if second == 60:
            second = 0
            minute+=1
        if minute == 60:
            minute = 0
            hours+=1
        os.system('cls')
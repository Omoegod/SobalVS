import os
from time import sleep
from datetime import datetime
from digits import round_five, round_four, round_one, round_three, round_two

def clock():
    while True:
        try:
            os.system("cls")
            clock = datetime.now()
            hour = str(clock.hour)
            minute = str(clock.minute)
            second = str(clock.second)
            if(len(hour) < 2):
                hour = "0" + hour
            if(len(minute) < 2):
                minute = "0" + minute
            if(len(second) < 2):
                second = "0" + second
            print(round_one[hour[0]],round_one[hour[1]],round_one[':'],round_one[minute[0]],round_one[minute[1]],round_one[':'],round_one[second[0]],round_one[second[1]])
            print(round_two[hour[0]],round_two[hour[1]],round_two[':'],round_two[minute[0]],round_two[minute[1]],round_two[':'],round_two[second[0]],round_two[second[1]])
            print(round_three[hour[0]],round_three[hour[1]],round_three[':'],round_three[minute[0]],round_three[minute[1]],round_three[':'],round_three[second[0]],round_three[second[1]])
            print(round_four[hour[0]],round_four[hour[1]],round_four[':'],round_four[minute[0]],round_four[minute[1]],round_four[':'],round_four[second[0]],round_four[second[1]])
            print(round_five[hour[0]],round_five[hour[1]],round_five[':'],round_five[minute[0]],round_five[minute[1]],round_five[':'],round_five[second[0]],round_five[second[1]])
            sleep(0.49)
            os.system("cls")
            print(round_one[hour[0]], round_one[hour[1]], round_one[':'], round_one[minute[0]], round_one[minute[1]], round_one[':'], round_one[second[0]],round_one[second[1]])
            print(round_two[hour[0]], round_two[hour[1]], round_five[':'], round_two[minute[0]], round_two[minute[1]], round_five[':'], round_two[second[0]],round_two[second[1]])
            print(round_three[hour[0]],round_three[hour[1]], round_three[':'], round_three[minute[0]], round_three[minute[1]], round_three[':'], round_three[second[0]],round_three[second[1]])
            print(round_four[hour[0]],round_four[hour[1]], round_five[':'], round_four[minute[0]], round_four[minute[1]], round_five[':'], round_four[second[0]],round_four[second[1]])
            print(round_five[hour[0]],round_five[hour[1]], round_five[':'], round_five[minute[0]], round_five[minute[1]], round_five[':'], round_five[second[0]],round_five[second[1]])
            sleep(0.49)
        except:
            return

clock()

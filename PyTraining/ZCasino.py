__author__ = 'dleclair'

from random import randrange

myMoney = 1000
maxPlayMoney = 3
canContinue = True

while canContinue:
    playMoney = 0

    if myMoney < maxPlayMoney + 1:
        playMoney = randrange(1, myMoney + 1)
    else:
        playMoney = randrange(1, maxPlayMoney + 1)

    myMoney -= playMoney

    myNumber = randrange(0, 51)
    print("I gamble", playMoney, "on", myNumber)

    randomNumber = randrange(0, 51)
    print("random result is", randomNumber)

    if myNumber == randomNumber:
        winMoney = playMoney * 2
        myMoney += winMoney
        print("I win", winMoney, "!")
    else:
        print("I lost !")

    if myMoney < 1:
        canContinue = False
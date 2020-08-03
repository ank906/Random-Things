import time
import random

def giveHand():
    cardColor = ['r','y','g','b']
    cardType = ['1','2','3','4','5','6','7','8','9','0','skip','⇵','+2','+4','wild']

    rndcardType = cardType[random.randint(0,14)]
    rndcardColor = cardColor[random.randint(0,3)]
    print(rndcardColor + " " + rndcardType)



this = input("start gmae? [y/n]")

if(this == 'y'):
    print("thease are your cards : ")
    giveHand()
    giveHand()
    giveHand()
    giveHand()
    giveHand()
    giveHand()
    giveHand()




    

if(this == 'n'):
    print("dont run the script if ur not gonna play stupid")
    time.sleep(3)
    exit()
    



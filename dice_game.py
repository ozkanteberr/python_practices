import random

while True : 
    decide=input("Zar atmak ister misiniz(y/n)?:").lower()

    if(decide=='y'):
        print(f'({random.randint(1,6)},'+ f'{random.randint(1,6)})')
    elif (decide=='n'):
        print("Oynadıgın icin tesekkurler!")
        break
    else:
        print("Gecersiz secim!")     
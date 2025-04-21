import random
from warnings import catch_warnings

random_number = random.randint(1,100)

while True:
    try:
        guess = int(input("Tahmininizi girin(1-100):"))
        if guess < 0 or guess > 100:
            print("Lutfen 1-100 arası deger girin")
        else:
            if guess == random_number:
                print(f"Tebrikler dogru tahmini buldun! Tuttugum sayı {random_number} idi.")
                break
            elif guess < random_number:
                print("Daha yuksek degerde bir tahminde bulun")
            elif guess > random_number:
                print("Daha dusuk degerde bir tahminde bulun")
    except ValueError:
        print("Lutfen sayi girin!")
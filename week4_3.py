''' Emrah CINAR 02/01/21
Number Guessing Game
'''
import random #rastgele sayi icin random modulu import edilir,
import time  #sure hesaplamak icin time modulu import edilir,
randomNumber=random.randint(1,100) #rastgele sayi tespiti yapilir,
guess_count=0 #oyuncunun tahhmin sayisi icin sayc
while True:
    guess_count+=1 #her tahmin girisinde sayac bir artar
    start=time.time() #oyun baslangi zamani
    user_guess=int(input("Enter a guess: "))
    if user_guess==randomNumber: #kullanici girisi ile rastgle secilen sayi esit ise
        stop=time.time() #oyun bitis zamani
        print(f'You knew in {guess_count} guesses. Time:{(stop-start):.3}') #bitis zamanindan baslangic zamani cikarilir 
        break         #f string ile tahmin(guess_count) ve sure yazdirilir.    
    elif user_guess<randomNumber: #tahmin kucuk ise kullanici sayiyi buyutmesi icin uyarilir
        print("UP")
    elif user_guess>randomNumber:
        print('DOWN')               
    
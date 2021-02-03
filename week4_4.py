'''Emrah CINAR PyCoders 02/02/21'''
    #''' olusturulan moduller import edilir'''
from total import total
from subtract import subtract 
from multiplication import multiplication
from division import division

print("islem secmek icin (+), (-), (x), (/) isaretlerini kullanin ")
       
user_ingang=(input("calc programina hosgeldiniz devam etmek icin 'Y' cikmak icin 'N' tusuna basin"))  
user_ingang=user_ingang.lower()                              
while user_ingang=="y":  
    try:                #''' kullanicidan girdiler alinir. hata ayiklamasi icin try except blogunda '''
        user_kies=input("islem sec:")
        sayi1=float(input("sayi gir: "))
        sayi2=float(input("sayi gir:"))        
                
        if user_kies=="+":
                print(total(sayi1,sayi2))                
        if user_kies=="-":
                print(subtract(sayi1,sayi2)) #kosullar karsilandiginda ilgili modulden fonksiyon cgrilir islem yapilir,
        if user_kies=="x":
                print(multiplication(sayi1,sayi2))
        if user_kies=="/":
                print(division(sayi1,sayi2))
        else:
                print('lutfen (+,-,x,/) isaretlerini kullanin') #kullanici isaret yanlis girdigi durumlarda
        user_ingang=(input('yeniden hesaplamak icin "Y" tusuna basin cikmak icin "N" '))#islem sonrasi tekrar kullaniciya sorulur.
        user_ingang=user_ingang.lower()
        if user_ingang=="n":
            print("programdan cikiliyor...")
        
    except ValueError: 
        print("Lutfen sayi giriniz") #Kullanici tarafindan girilecek hatali giris durumunda calistirilacak mesaj
if user_ingang=="n":
        print("programdan cikiliyor...") #kullanici ilk giriste cikmak isterse 

                
    
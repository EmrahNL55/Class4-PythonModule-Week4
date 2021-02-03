import math #math modulu import edilir
sayilar=[]  
while len(sayilar)<4:# 4 sayinin okeki bulunacagi icin
    try: #kullanicidan gelecek hatalar icin hata ayiklama kullasnilir,
        user=int(input('Ekok icin sayi giriniz:')) #giris alinir
        sayilar.append(user) #alinan girisler sayilar isimli listeye eklenir,
    except ValueError: #yanlis gris yapilip ValueError hatasi icin,
        print('Lutfen sayi giriniz.')
#''' listenin 0 ve 1. indeksindeki syilarin obebi ile 2.ve 3. indeksindekilerin obebi carpilarak  okekleri bulunur  
    #math.gcd ile obebleri bulunur,
ekok_func=(lambda a,b: math.gcd(a,b))(sayilar[0],sayilar[1])*(lambda a,b: math.gcd(a,b))(sayilar[2],sayilar[3])    

print(f'{sayilar} sayilarinin EKOKU:{ekok_func} dir.')
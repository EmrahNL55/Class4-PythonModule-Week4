'''Emrah CINAR 01/31/21 21:40 '''
'''password generation program'''

import tkinter as tk
import random

def generate():  
    chars_tpl=('?>_<&!@*#%£§-æ')
    numbers_tpl=('01234567899876543210')
    bletters_tpl=('ABCDEFGHIJKLMNOPRSTUVYZ')
    kletters_tpl=('abcdefghıjklmnoprstuvyz')    
    list_password=[]
    list_fr=chars_tpl,numbers_tpl,bletters_tpl,kletters_tpl #tupllar degiskene atanir 
    
    while len(list_password)<10: 
        for i in list_fr: #tupl verileri i degiskenine atanir  
            list_password.append(i[random.randint(0,(len(i)-1))]) # i degisken uzunlugu tespit edilip,0 dan uzunluga kadar randint ile rastgele  
            if len(list_password)==10:   #rakam secilir.i[] ile bu rakam index olarak kullanilip, indexin karsiligi olan rakam append ile listeye eklenir,
                           
                label['text']=("".join(list_password)) #eklenen karakter uzunlugu 10 oldugunda bu satir ile labele gonderilir  
                                                        #orada bulunan text ile degistirilir ve pencerede gosterilir,
root = tk.Tk()
root. title('Generate Password  by emrah') #pencere adi
root.geometry("350x250+575+50")  #pencere boyutlari ve ekrandaki konumu
label=tk.Label(text='sifreniz',fg="white",bg="black",padx=20,pady=20) #sifrenin gosterildigi etiket 
label.pack() #labelin gosterilmesini saglayan satir
button_password=tk.Button(root, text='Generate',fg="blue",padx=20,pady=20,command=generate) #dongunun calismasini saglayan button (command=generate)
button_password.pack()

root.mainloop() #pencerenin devamli olarak gorunmesini saglar

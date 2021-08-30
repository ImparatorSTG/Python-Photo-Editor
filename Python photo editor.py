from PIL import Image
import numpy as np 
import time
def renk_degisimi():
    h=pic.shape[0]
    w=pic.shape[1]
    newpic=np.zeros((h ,w ))
    for i in range(h):
        for j in range(w):
            newpic[i][j]+=pic[i][j][0]*0.2989+pic[i][j][1]*0.5870+pic[i][j][2]*0.1140
    matrix2=[]
    for i in range(3):
        b =[] 
        for j in range(3):
            b.append(int(input())) 
        matrix2.append(b)
    
def kirpma():
    x1=int(input("x1 değerini giriniz: "))
    
 
    

def terscevir():
    tersfoto = pic.copy()
    tersfotos=tersfoto[::-1]
    son=Image.fromarray(tersfotos)
    son.show()
secim=input("1-Resim Ekleyin\n2-Resmi siyah ve beyaz hale çevirin\n3-Resmi ters çevirin\n4-Çıkış\nSeçiminizi giriniz: ")
while secim!="1" and secim!="2" and secim!="3" and secim!="4":
    time.sleep(1)
    print()
    print("Lütfen seçeneklerden birini giriniz.")
    print()
    time.sleep(1)
    secim=input("1-Resim Ekleyin\n2-Resmi siyah ve beyaz hale çevirin\n3-Resmi ters çevirin\n4-Çıkış\nSeçiminizi giriniz: ")
print()
while secim=="2" or secim=="3":
    time.sleep(0.5)
    print("İşlem yapmadan önce resim yüklemeniz gerekmektedir\n")
    time.sleep(1)
    secim=input("1-Resim Ekleyin\n2-Resmi siyah ve beyaz hale çevirin\n3-Resmi ters çevirin\n4-Çıkış\nSeçiminizi giriniz: ")
    while secim!="1" and secim!="2" and secim!="3" and secim!="4":
        print("Lütfen seçeneklerden birini giriniz.")
        secim=input("1-Resim Ekleyin\n2-Resmi siyah ve beyaz hale çevirin\n3-Resmi ters çevirin\n4-Çıkış\nSeçiminizi giriniz: ")

while True:
    while secim=="1":
        picture=input("Lütfen yüklemek istediğiniz resmin adını giriniz(örnek: resim.jpg): ")
        print()
        time.sleep(1)
        print("{} resmi yüklendi".format(picture))
        print()
        time.sleep(1)
        picture_open=Image.open(picture)
        pic=np.array(picture_open)
        secim=input("1-Resim Ekleyin\n2-Resmi siyah ve beyaz hale çevirin\n3-Resmi ters çevirin\n4-Çıkış\nSeçiminizi giriniz: ")
        while secim!="1" and secim!="2" and secim!="3" and secim!="4":
            print("Lütfen seçeneklerden birini giriniz.")
            secim=input("1-Resim Ekleyin\n2-Resmi siyah ve beyaz hale çevirin\n3-Resmi ters çevirin\n4-Çıkış\nSeçiminizi giriniz: ")
        print()
    while secim=="2":
        renk_degisimi()
        secim=input("1-Resim Ekleyin\n2-Resmi siyah ve beyaz hale çevirin\n3-Resmi ters çevirin\n4-Çıkış\nSeçiminizi giriniz: ")
        while secim!="1" and secim!="2" and secim!="3" and secim!="4":
            print("Lütfen seçeneklerden birini giriniz.")
            secim=input("1-Resim Ekleyin\n2-Resmi siyah ve beyaz hale çevirin\n3-Resmi ters çevirin\n4-Çıkış\nSeçiminizi giriniz: ")
        print()
    while secim=="3":
        terscevir()
        secim=input("1-Resim Ekleyin\n2-Resmi siyah ve beyaz hale çevirin\n3-Resmi ters çevirin\n4-Çıkış\nSeçiminizi giriniz: ")
        while secim!="1" and secim!="2" and secim!="3" and secim!="4":
            print("Lütfen seçeneklerden birini giriniz.")
            secim=input("1-Resim Ekleyin\n2-Resmi siyah ve beyaz hale çevirin\n3-Resmi ters çevirin\n4-Çıkış\nSeçiminizi giriniz: ")
        print()
    while secim=="4":
        print("Çıkış yapılıyor.")
        time.sleep(1)
        quit()
    
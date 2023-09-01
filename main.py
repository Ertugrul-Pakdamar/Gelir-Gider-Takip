

bakiye = []
gelirAçıklaması = []
gider = []
giderAçıklaması = []
borç = []
borçAçıklaması = []
alınacak = []
alınacakAçıklaması = []

def TümünüGöster():
    BakiyeYazdırma()
    
    print("\nTüm Gelirleriniz:")
    for i in range(int(len(bakiye))):
        print("\n" + gelirAçıklaması[i])
        print(bakiye[i])
    
    print("\nTüm Giderleriniz:")
    for i in range(int(len(gider))):
        print("\n" + giderAçıklaması[i])
        print(gider[i])
        
    print("\nTüm Borçlarınız:")
    for i in range(int(len(borç))):
        print("\n" + borçAçıklaması[i])
        print(borç[i])
    
    print("\nTüm Alacaklarınız:")
    for i in range(int(len(alınacak))):
        print("\n" + alınacakAçıklaması[i])
        print(alınacak[i])
    
    

def BakiyeYazdırma():
    bakiyeToplamı = 0
    for i in range(0, int(len(bakiye))):
        bakiyeToplamı = bakiyeToplamı + bakiye[i]
    for j in range(0, int(len(alınacak))):
        bakiyeToplamı = bakiyeToplamı - alınacak[j]
    for k in range(0, int(len(borç))):
        bakiyeToplamı = bakiyeToplamı + borç[k]
        
    print("\nMevcut bakiyeniz " + str(bakiyeToplamı) + "TL")  

def GelirEkle(tutar):
    açıklama = str(input("Gelir açıklamasını giriniz(opsiyonel): "))
    bakiye.append(tutar)
    gelirAçıklaması.append(açıklama)
    BakiyeYazdırma()

def GiderEkle(tutar):
    açıklama = str(input("Gider açıklamasını giriniz(opsiyonel): "))
    gider.append(tutar)
    giderAçıklaması.append(açıklama)
    
    print("Tüm Giderleriniz:")
    for i in range(int(len(gider))):
        print("\n" + giderAçıklaması[i])
        print(gider[i])
    
    BakiyeYazdırma()
    
    
def BorçEkle(tutar):
    açıklama = str(input("Borç açıklamasını giriniz(opsiyonel): "))
    borç.append(tutar)
    borçAçıklaması.append(açıklama)
    
    print("Tüm Borçlarınız:")
    for i in range(int(len(borç))):
        print("\n" + borçAçıklaması[i])
        print(borç[i])
        
    BakiyeYazdırma()

def AlınacakEkle(tutar):
    açıklama = str(input("Alınacak açıklamasını giriniz(opsiyonel): "))
    alınacak.append(tutar)
    alınacakAçıklaması.append(açıklama)
    
    print("Tüm Alacaklarınız:")
    for i in range(int(len(alınacak))):
        print("\n" + alınacakAçıklaması[i])
        print(alınacak[i])
        
    BakiyeYazdırma()

while True:
    print("1-Gelir Ekle")
    print("2-Gider Ekle")
    print("3-Borç Ekle")
    print("4-Alınacak Ekle")
    print("5-Tümünü Göster")
    tercih = int(input("Tercih: "))

    if tercih == 1:
        tutar = int(input("Lütfen eklenecek gelirin tutarını giriniz: "))
        GelirEkle(tutar)
    elif tercih == 2:
        tutar = int(input("Lütfen eklenecek gider tutarını giriniz: "))
        GiderEkle(tutar)
    elif tercih == 3:
        tutar = int(input("Lütfen alınacak borç tutarını giriniz: "))
        BorçEkle(tutar)
    elif tercih == 4:
        tutar = int(input("Lütfen verilecek borç tutarını giriniz: "))
        AlınacakEkle(tutar)
    elif tercih == 5:
        TümünüGöster()
    else:
        print("İşlem başarısız lütfen tekrar deneyiniz.\n")



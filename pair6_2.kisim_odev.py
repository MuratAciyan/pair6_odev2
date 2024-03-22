#SORU1:
fibonacci_seri = [1, 1]

while len(fibonacci_seri) < 20:
    yeni_eleman = fibonacci_seri[-1] + fibonacci_seri[-2]
    fibonacci_seri.append(yeni_eleman)

print(fibonacci_seri)

#SORU2:
dizi=[]
toplam=0
Mukemmel_sayi=int(input("bir sayı giriniz:"))
for i in range(1,Mukemmel_sayi):
    if Mukemmel_sayi%i==0:
        dizi.append(i)
        toplam+=i
if toplam==Mukemmel_sayi :
    print(f"bu sayı mükemme bir sayi bu =>{dizi} bölenlerin toplamı={toplam}")
else:
    print("girdiğin sayı mükemmel değil")

#SORU3:

def ebob_bul(sayi1, sayi2):
    while sayi2 != 0:
        sayi1, sayi2 = sayi2, sayi1 % sayi2
    return sayi1

def ekok_bul(sayi1, sayi2):
    return (sayi1 * sayi2) // ebob_bul(sayi1, sayi2)

sayi1 = int(input("Birinci sayiyi giriniz "))
sayi2 = int(input("İkinci sayiyi giriniz "))

ebob = ebob_bul(sayi1, sayi2)
ekok = ekok_bul(sayi1,sayi2)

print(f"{sayi1} ve {sayi2} sayılarının EBOB'u: {ebob}")
print(f"{sayi1} ve {sayi2} sayılarının EKOK'u: {ekok}")

#SORU4:
sayi= int(input("Lütfen bir sayı giriniz : "))
if sayi>1:

    for i in range (2,sayi):
        if (sayi% i) ==0:
            print ("Sayi asal değildir")
            break
    else :
        print("Sayi asaldır")


#SORU5:
def asal_carpanlari_bul(sayi):
    asal_carpanlar = []
    carpan = 2  # Asal çarpanları bulmak için başlangıç değeri

    while carpan * carpan <= sayi:
        if sayi % carpan == 0:
            asal_carpanlar.append(carpan)
            sayi //= carpan  # Sayıyı böldükçe küçült
        else:
            carpan += 1

    if sayi > 1:
        asal_carpanlar.append(sayi)

    return asal_carpanlar

sayi = int(input("Bir sayı girin: "))
asal_carpanlar = asal_carpanlari_bul(sayi)
print(f"{sayi} sayısının asal çarpanları: {asal_carpanlar}")

#LAPORAN TUGAS KECIL 1 - CRYPTARITHMETIC
#NAMA: Leonard Matheus
#NIM : 13519215
#Strategi Algoritma
#Kelas : K-4

import sys
import time

def find_letter(let, lst):
    #mengecek apakah ada huruf yang sama di dalam array sebelum dimasukkan
    return (lst or False) and \
           ((isinstance(lst[0], str) and let in lst[0]) or find_letter(let, lst[1:]))

def masukkanInput(namafile):
    f = open(namafile,"r") #membuka file
    for x in f:
        x = x.replace("\n", "") #membersihkan tanda enter
        print(x)

def bacafile(namafile):
    data = [] #list kosong untuk input
    huruf = [] #list kosong untuk hurufnya
    f = open(namafile,"r")
    for x in f:
        x = x.replace("\n", "") #membersihkan tanda enter
        print(x)
        x = x.replace("-", "") #membersihkan tanda ------
        x = x.replace("+", "") #membersihkan tanda +
        x = x.replace(" ", "") #membersihkan tanda spasi
        data.append(x)
        for y in x:
            if (find_letter(str(y), huruf)==False) and (y.isalpha()==True):
                #input huruf unik saja ke list huruf
                huruf.append(y)
    data = list(filter(None, data)) #membuang elemen kosong
    f.close()
    return data,huruf

def permutasi(lst, n): 
    #Cara Pakai: permutasi([x for x in <listnya>], n)
    if n == 0:
        return [[]] #bila 0, return list kosong
    l = []
    for i in range(0, len(lst)): 
        m = lst[i] 
        temp = lst[:i] + lst[i+1:]
        for p in permutasi(temp, n-1): #rekursif
            l.append([m]+p) 
    li = [[int(j) for j in i] for i in l] #konversi tipe data non-type ke integer
    return li

def katangka(kata, coba):
    #Mengubah kata ke angka dalam bentuk integer
    return int(''.join(str(coba[huruf]) for huruf in kata))

def solusi(data, huruf):
    angka = "0123456789" #digit angka yang mungkin
    data = [kata.upper() for kata in data] #membuat semua huruf jadi huruf besar
    jawab = [] #untuk menampung jawaban angka yang cocok
    percobaan = 0 #untuk menghitung proses
    if len(huruf) > 10:
        print("Huruf kebanyakan, maksimal 10 ya!")
    else:
        for i in permutasi(angka,len(huruf)):
            coba = dict(zip(huruf, i)) #kombinasi dictionary huruf dan pasangan angka yang benar
            percobaan += 1 #menghitung jumlah percobaannya
            if all((coba[kata[0]] > 0) for kata in data): #membatasi huruf awal tidak boleh 0
                bilangan = [katangka(kata, coba) for kata in data] #memngubah operan -> kata jadi integer
                if sum(bilangan[:len(data)-1]) == bilangan[len(data)-1]: #bila hasilnya cocok
                    jawab.append(bilangan)
    return jawab, percobaan

def tampilkanLayar(arr1):
    if (len(arr1)==0): #Jika panjang arraynya 0, tidak ada solusi ya kan
        print("TIDAK ADA SOLUSI YANG MUNGKIN") 
    else:
        print("SOLUSI YANG MUNGKIN ADALAH:")
        for i in range(len(arr1)): #panjang operan + hasil
            for j in range(len(arr1[i])): #jumlah digit
                if (j == (len(arr1[i])-1)): #bila ternyata i= angka iterasi sebelum hasil, tambahkan "------"
                    for k in range (len(str(arr1[i][j]))+3):
                        print("-",end="")
                    print("")
                    print(str(arr1[i][j]))
                if (j == (len(arr1[i]))-2): #tambahkan "  "
                    for m in range (len(str(arr1[i][-1]))-(len(str(arr1[i][j])))):
                        print(" ",end="")
                    print (str(arr1[i][j]),"+")
                elif ((j != (len(arr1[i])-1)) and (j != (len(arr1[i]))-2)) :
                    for m in range (len(str(arr1[i][-1]))-(len(str(arr1[i][j])))):
                        print(" ",end="")
                    print(str(arr1[i][j]))
            print("")

def converttxt(namafile, arr1, waktu, percobaan): #ubah ke file txt
    sys.stdout = open("hasil.txt", "w")
    masukkanInput(namafile)
    print("")
    tampilkanLayar(arr1)
    print("Waktu yang dibutuhkan adalah", waktu, "detik")
    print("Percobaan yang telah dilakukan untuk menemukan kombinasi cryptarithhmetic :", percobaan, "kali")
    sys.stdout.close()

#Program Utama
awal = time.time() #waktu mulai
namafile = "input.txt" #nama file
data,huruf = bacafile(namafile) #membaca input file txt
print("")
arr1, percobaan = solusi(data, huruf)
tampilkanLayar(arr1)
akhir = time.time() #waktu akhir
waktu = float(akhir-awal) 
print("Waktu yang dibutuhkan adalah", waktu, "detik")
print("Percobaan yang telah dilakukan untuk menemukan kombinasi cryptarithhmetic :", percobaan, "kali")
converttxt(namafile,arr1,waktu,percobaan) #menyalin ke file txt hasil
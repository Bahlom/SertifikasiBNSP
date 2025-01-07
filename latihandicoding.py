name= input('masukkan nama anda:')
umur= int(input('masukkan umur anda:'))
umur_ditahun_2024 = 2024 - (umur)
print(f'anda lahir pada tahun {umur_ditahun_2024} kan')
mhs = 'Mahasiswa UBSI'
print('selamat datang', name)
print(mhs)
print(f'selamat datang {mhs}', name)

'''List  = - seperti array tp isinya bisa beda2 type data
           - bisa diindex [0], dan slice
           - data bisa diubah
           - logo [] dipisahkan koma
    Tuple= - isinya bisa beda2
           - bisa diindex [0], dan slice
           - data tidak bisa diubah
           - logo () dipisahkan koma
    set=   - isi beda2
           - tidak bisa diindex
           - tidak bisa diubah
           - logo {} dipisahkan koma
           - tidak ada duplikat
           - bisa melakukan .union()” dan “.intersection()
    dict=  - isi beda2 tapi 
           - tidak bisa diindex
           - bisa diubah
           - logo {} dipisahkan koma
           - terdiri dari key:value
           - bisa melakukan .keys() dan .values()
           - bisa melakukan .update() dan .pop()
           - bisa melakukan .get() dan .items()
           - bisa melakukan .clear() dan .copy()
           - bisa melakukan .pop() dan .popitem()
           - bisa melakukan .setdefault() dan .update()
           - menambah data x ['Job'] = "Web Developer"
           - menghapus data x.pop('Job') atau del x['isMarried']
           - mengubah data x['isMarried'] = True
           - Konversi list dari beberapa tuple yang isinya pasangan nilai menjadi dictionary print(dict([(3,26),(4,44)]))
'''


data = [1, 2.2, 'Dicoding']
print(data[0:3])

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }

print(x ['name'])

'''transformasi data
- kata.upper()
- kata.lower()
- kata.capitalize()
- kata.title()
- kata.split()
- kata.strip()
- kata.replace()
- kata.splitlines()
- .join() print('123'.join(['Dicoding','Indonesia']))
- st1 = "Jum'at"
'''

kata = 'dicoding'
kata = kata.upper()
print(kata)

'''Operasi pada List, Set, dan String
- len() jumlah list
- min,max
- print(genap.count(6)) menghitung banyaknya angka 6
- in not in hasilnya true
- memberi nilai : data = ['shirt', 'white', 'L']   apparel, color, size = data (nanti hasilnya sesuai urutan)
- variabel.sort() tdk bisa sort angka dan huruf dalam satu list
- variabel.sort(reverse=True) descendig
'''

'''Ekspresi print(x + y) --- <operan1> <operator> <operan2> di bagi 2:
1 banyaknya operan 
- operator aritmatika : (x + y), (x - y), (x * y), (x / y), (x ** y), (x < y), (x <= y), (x > y), (x >= y), (x % y), (x == y), (x != y). dan (x += 1), (x-=1), (not x).
contoh : 
b = 6 
b -= 1
print(b) hasil = 5
- operator logika : and, or, not
2. Ekspresi Menurut Tipe Data yang Dihasilkan
  - <numerik> <operator> <numerik> = <numerik> 2 + 2 = 4 aritmatika
  - <numerik> <operator> <numerik> = <boolean> 3 < 10 = True relasional(hasilnya selalu boolean) contoh x==y Menghasilkan True, jika kedua operan bernilai sama.
  - <boolean> <operator> <boolean> = <boolean> True or False = True (logika)

Untuk yg bertype string, dihitung jumlah karakternya
- operator assignment (+=,dll) contohnya:
    x = 11
    x += 5
    print(x)

    sama aja kaya 

    x = 11
    x = x + 5
    print(x)
    hasilnya sama2 16
'''

dico = 750000

# TODO: Silakan buat kode Anda di bawah ini.

if dico > 500000:
    diskon = 0.10 * dico
    total_harga = dico - diskon
else:
    total_harga = dico

print(total_harga)

'''python di tulis secara skuensial/berurutan. 
    jika error indented block,berarti kurang rapih programnya/kurang spasi menjorok ke dalam.Error dihasilkan karena harusnya terdapat indentasi (biasanya berupa empat spasi) sebelum kode "print(i)
    case-sensitive bgt pd variabelnya
    x, y = y, x    # One-liner
    '''

'''error dan exception handling percabangan & perulangan
 - percabangan (nilai if adalah true jika ada isinya) if,elif, else (jika if berisi false,maka else di jalankan(opsional sifatnya)):
    ketersediaan = "Daging ayam"

        if ketersediaan == "Daging ayam":
            print("Ibu membeli dan memasak ayam")
        else:
            print("Ibu membeli dan memasak tempe")

        """
        Output:
        Ibu membeli dan memasak ayam
        
    #One Liner: score = 100
    if score == 100: print("Nilai Anda sempurna!")

    bisa pake'and' atau 'or' operator dalam kondisi percabangan
   
'''
#one Liner (block kode benar if kondisi else block kode salah)
ketersediaan = "Daging ayam"
print('ibu membeli ayam') if ketersediaan=="Daging ayam" else print('ibu membeli tempe')

nilai = 81
perilaku = 'tidak baik'

print('selamat kamu lulus dan baik') if nilai>= 80 and perilaku=='baik' else print('Coba lagi semester besok')

'''
- perulangan
    - perulangan/looping jgn lupa ":"
    - for (looping berdasarkan urutan/iterasi)
    - while (looping berdasarkan kondisi)
    - break (berhenti looping)
    - continue (melanjutkan looping ke iterasi berikutnya)
    - range (menghasilkan angka-angka berurutan)
    - enumerate (menghasilkan angka-angka berurutan dan indexnya)

 for i in range(10):
     print(i)
hasil 0-9 
syntak range() sbb: range(star,stop,step) yg wajib itu stop sja. 
perulangan urutan akan berhenti sebelum mencapai nilai stop : for i in range(1,10,2): hasilnya: 1,3,5,7

 while kondisi:
    blok pernyataan yang akan terus di ulang selama true   
'''
counter = 1
while counter <= 5:
    print(counter)
    counter += 1 #increment wajib untuk emmastikan loop berhenti

'''for bersarang/nested loop=perulangan dalam perulangan'''
print('nestedloop, hasilnya kiri i, kanan j')
for i in range(1,5):
    for j in range(1,5):
        print(i,j)
'''# hasil = program akan mengulang dari loop luar (1) kemudian turun ke loop dalam (1) sampe (4),
    jika loop dalam sudah selesai semua sampe (4,)maka balik ke loop luar lagi (2) dst'''

'''Kontrol Perulangan
# break dengan if
'''
for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 3:
            break  # Menghentikan perulangan dalam jika j = 3
# continue

for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))

#Else setelah For (untuk pencarian)
'''Pada else setelah for, statement else tidak akan dieksekusi saat if pernah sekali saja benar. 
    Dengan kata lain, break dalam if harus tidak terjadi untuk memicu else setelah for. makanya elsenya sejajar dengan for'''

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan.")

'''
Else setelah While
Berbeda dengan else setelah for, pada statement else setelah while, blok statement else akan selalu dieksekusi saat kondisi pada while menjadi salah. 
'''

count = 0

while count < 3:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")

#contoh lain

n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")

'''else tidak tercetak di sini. Hal ini disebabkan while tersebut masih bernilai benar walaupun program keluar karena "break"'''

#Pass (program tidak mencetak apapun)
x = 10

if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")

#List Comprehension =membuat sebuah list baru berdasarkan list yang sudah ada

angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
    pangkat.append(n**2)
print(pangkat)
#one linenya rumus new_list=[expression for ...]
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)


'''
1. syntax errors--> pd saat penguraian/penulisan perintah
 - IndentationError=(expected an indented block)kasih spasi 4x di tanda "^" (caret)
 - SyntaxErrors = (invalid syntax) misal kurang ":" pada for n while
 
 
2. exceptions--> pd saat beroperasi/di jalankan(pyton ngerti perintah tp bermasalah pd saat ngiutinnya)
 - c/ print(angka). NameError: name 'angka' is not defined. tidak mendefinisikan variabel angka terlebih dahulu
 - c/ bukan_angka = '1', bukan_angka + 2. TypeError: can only concatenate str (not "int") to str. int tidak bisa di tambah str
 - KeyError= error yg terjadi jika salah penulisan dalam pemanggilan key di data dictionary
 - ciri2 = ada traceback (most recent call last): ini adalah pelacakan jejak jalur ekseskusi program sebelum mencapai titik error
 - penanganan exception/pengecualian:  try-except
    jika ada error seperti ini:
    z = 0
    print(1/z) #nol tidak bisa untuk membagi
    output:
    Traceback (most recent call last):
    File "/home/glot/main.py", line 2, in <module>
    print(1/z)
    ZeroDivisionError: division by zero

    #penanganannya menggunakan try-except:
    z = 0
    try:
        print(1/z)
    except ZeroDivisionError:
        print("Anda tidak bisa membagi angka dengan nilai nol.")
    output:
    Anda tidak bisa membagi angka dengan nilai nol.
  - try-except. Berikut strukturnya(biasanya hanya sampai try-except saja):
    try: 
        (blok kode yang mungkin terjadi pengecualian)
    except:
        (pernyataan yang dioperasikan jika terjadi pengecualian)
    else:
        (pernyataan yang dioperasikan jika TIDAK terjadi pengecualian,jadi jika kode ga error,block statement ini tetap nampil di output)
    finally:
        (pernyataan yang di operasikan setelah semua pernyataan diatas terjadi/Kode ini dieksekusi terlepas dari ada atau tidaknya except)
   #contoh:
    var_dict = {"rata_rata": "1.0"}

        try:
            print(f"rata-rata adalah {var_dict['rata_rata']}")
        except KeyError:
            print("Key tidak ditemukan.")
        except TypeError:
            print("Anda tidak bisa membagi nilai dengan tipe data string")
        else:
            print("Kode ini dieksekusi jika tidak ada exception.")
        finally:
            print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")
            
        """
        Output:
        rata-rata adalah 1.0
        Kode ini dieksekusi jika tidak ada exception.
        Kode ini dieksekusi terlepas dari ada atau tidaknya exception.
        """
3. Raise exception = Kesalahan di sengaja (2 error di atas kesalahan tidak disengaja)  
    umumnya digunakan pada if-else
    var = -1
        if var < 0:
            raise ValueError("Bilangan negatif tidak diperbolehkan")
        else:
            for i in range(var):
                print(i+1)
    output: 
    Traceback (most recent call last):
        File "/home/glot/main.py", line 3, in <module>
            raise ValueError("Bilangan negatif tidak diperbolehkan")
    ValueError: Bilangan negatif tidak diperbolehkan
'''
'''
Array =sebuah kelompok besar yang terdiri dari beberapa nilai atau data (type data harus sama).
array merupakan salah satu jenis struktur data linear dan terdiri dari kumpulan elemen bertipe data sama dengan indeks yang berurutan atau linear. 
Struktur data = adalah cara untuk mengatur dan menyimpan data sehingga data-data tersebut dapat diakses dan bekerja secara efisien.ada hubungan dan bisa beroperasi dengan setiap data tsb
liblary adalah kode program yang di buat oleh programmer lain untuk bisa di gunakan oleh progrmmer lainnya.
modul adalah file berisikan kode python dapat digunakan kembali. nanti di dlm modul ada fungsi2 yg bisa digunakan setelah kita import modulnya.
   
    import array

    x = array.array("i",[1, 2, 3, 4, 5]) #i adalah int
    print(x)
    print(type(x))

'''
z = 0
try:
    print(1/z)
except:
    print("Error")

'''
proses squensial pd array
Variabel "i" bertindak sebagai indeks saat ini yang digunakan untuk mengakses elemen dalam setiap iterasi atau perulangan.

var_arr = [1, 2, 3, 4, 5]

for i in range(len(var_arr)):
    current_element = var_arr[i]
    next_index = i+1
    
    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None
        
    print(f"Current element: {current_element}, next elements: {next_element}")

'''
#mencari nilai terbesar dari array
var_arr = [1, 7, 2, 89, 3]
left_point= var_arr[0]

for i in range(1,len(var_arr)):
    right_point=var_arr[i]

    if right_point > left_point:
        left_point=right_point

print(left_point)

var_array = [i for i in range(101)]

total_sum=0
for angka in var_arr:
    total_sum += angka

jumlah_element= len(var_arr)

hasil=(total_sum/jumlah_element)

print('nilai rata2:',hasil)

'''
matriks adalah kumpulan data yang diatur dalam bentuk tabel dua dimensi dengan setiap elemennya terdefinisi 
berdasarkan baris dan kolom. Matriks dalam pemrograman diimplementasikan menggunakan array dua dimensi. 
Bahkan dalam Python, matriks dapat diimplementasikan menggunakan nested list atau list di dalam list.
-bisa di tulis dengan nested list namum memakan banya memori, makanya kalau besar pakai numpy
-bisa di index
-harus type data yg sma (meskipun di pyton bisa beda)
-opsi operasi matematika yang bisa dilakukan: penjumlahan, pengurangan
-
'''
import numpy

matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
print(matriks)

'''
Deklarasi Matriks
1. Deklarasi sekaligus inisialisasi nilai matriks : 
matriks = [[1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1]]

2. Deklarasi dengan nilai default yang telah di sepakati bersama.. misal nilainya 1-10.  Kita bisa menyepakati nilai "0" sebagai nilai default karena di luar jangkauan yang disepakati (1-10)
  atau bisa juga dengan Cara kedua ini melibatkan list comprehension yang sama seperti pada materi array.

  a. default (nested list dan nested for)
     struktur : 
    <nama-var> = [[<default-val> for j in range (<m>)] for i in range(<n>)]
    contoh:
    matriks = [[0 for j in range(4)] for i in range(3)]

        print(matriks)

        Output:
        [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    
  b. list comprehension

    kuadrat = [x**2 for x in range(5)]
    print(kuadrat)
Akses Elemen Matriks

struktur:
<nama-var> = [nbrs][nkol] [selalu dimulai dari 0]

pada matriks dibawah ini kita mau mengkases element 12. yang terletak pada baris ke 2 kolom ke 1  atau bisa di tulis [2][1]

var_mat = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]
           
print(var_mat[2][1])


Output:
12
'''

'''Operasi Matriks pada Python

1. # mengalikan element matrix dengan konstanta tanpa numpy
    var_mat = [[5, 0],
            [1, -2]]
    def_mat = [[0 for j in range(2)] for i in range(2)]

    for i in range(len(var_mat)):
    for j in range(len(var_mat[0])):
        def_mat[i][j] = var_mat[i][j]*2

    print(def_mat)

    # dengan numpy

        import numpy as np

        var_mat = np.array([[5, 0],
                            [1, -2]])

        result = var_mat * 2

        print(result)

Anda masih bisa bereksplorasi dengan operasi matriks lainnya seperti transpose matriks, inverse matriks,dll
'''

'''Fungsi (def - return)
    struktuer header(def) (:) + body(indentasi block code) + return(back to varibel fungsi setelah eksekusi)

    Memanggil Fungsi
kita bisa memanggil fungsi dengan cara menuliskan nama fungsi seperti kita menggunakan "print()"
namun,untuk menampilkan hasilnya,dibutuhkan variabel lagi spt: (rumus_persegi_panjang_satu) 
'''

def rumus_luas_persegi_panjang(panjang,lebar):
    luas = panjang * lebar
    return luas

persegi_panjang_satu= rumus_luas_persegi_panjang(5,10)
print(persegi_panjang_satu)

#menggunakan lambda
#struktur lambda : func=lambda args:ret_val

mencari_luas_persegi_panjang= lambda panjang,lebar: panjang*lebar
print(mencari_luas_persegi_panjang(5,10))

'''- Isi fungsi dalam lambda dapat Anda ganti menjadi sebuah nilai, alih-alih variabel misal panjang*lebar di ganti int 5*10 langsung contoh: lambda panjang, lebar: 50 (tp nilainya akan tetap 50 terus)
   - Sebuah fungsi lambda dapat menerima argumen dalam jumlah berapa pun, tetapi hanya mengembalikan satu nilai ekspresi misal:tambahin args selain panjang n lebar, tetapi hanya 1 operasi yaitu panjang*lebar saja yg dieksekusi
'''

'''
BUat sipenhao dengan fungsi2 yg berbeda,klo bisa buat docsstringya.. kalau bisa ada one linernya'''

'''*args
def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1, 2, 3))

**kwargs (dictionary)

def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))

Output:
nama: Dicoding, usia: 17, pekerjaan: Python Programmer,
'''

'''scope variable
- global scope: variabel yang dideklarasikan di luar fungsi

    a = 10

    def add(b):
        result = a+b
        return result

    bilanganPertama = add(20)
    print(bilanganPertama)

    variabel a di deklarasikan di luar fungsi agar bisa di gunakan di seluruh program

- local scope: variabel yang dideklarasikan didalam fungsi

    def add(a, b):
        lokal_var = 5
        result = a+b-lokal_var
        return result

    bilanganPertama = add(10,20)
    print(bilanganPertama)

    Output:
    25
'''

'''modul
- masukkan 2 file pada folder yg sama dengan format .py (hello.py dan main.py)
- pemanggilan file hello dengan import di main

    import hello
    
    persegi_panjang_pertama = hello.mencari_luas_persegi_panjang(5,10)
    print(persegi_panjang_pertama)

    ------------------------------------------------
    bisa memanggil variabel jg
    nama = "Dicoding Indonesia" (pada hello.py)
    print(hello.nama) (pada main.py)

Terlihat pada kode di atas bahwa untuk menampilkan variabel kita tidak menggunakan kurung tutup "()" seperti pada saat pemanggilan fungsi. Namun, kita tetap menggunakan "hello" sebagai modul yang telah kita impor sebelumnya.
'''
#kita tidak perlu menulis hello. lagi jika diimport ada from nya
'''
from hello import mencari_luas_persegi_panjang, nama
 
persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)
 
print(nama)
'''
#quiz

def minimal(a,b):
    if a<b:
        return a
    elif b<a:
        return b
    else:
        return a

print(minimal(1, 4))
print(minimal(4, 4))
print(minimal(5, 3))

'''Sub Program Kedua = Prosedur
sama seperti fungsi hanya saja berupa def statement aja, ga ada return valuenya atau nilai/perintah2

def greeting(name):
    print("Halo " + name + ", Selamat Datang!")

    
greeting("Dicoding Indonesia")

"""
Output: 
Halo Dicoding Indonesia, Selamat Datang!
"""
'''

'''OOP in python

- duck typing = jika ia berjalan dan bersuara seperti bebek, maka kemungkinan besar ia adalah bebek

class = mobil (blueprint/cetakan)
atribut = warna, merk, tahun,kecepatan 160km/jam (identitas n aksesoris pendukung)
method = start, stop, gas, brake (perilaku)

jika class/blueprint sudah di buat, maka kita bisa membuat objek menggunakan blueprint tsb:
Objek merupakan perwujudan dari class dengan anggapan bahwa kelas adalah cetakan yang memungkinkan kita dapat membuat banyak objek berdasarkan cetakan tersebut.

objek = mobil_bahlom
atribut = idem
method = idem

bisa juga membuat kelas baru

kelas_baru= mobil_sport
atribut = idem
method = idem + turbo


class adalah keyword untuk membuat sebuah kelas dalam python
Saat kelas diwujudkan menjadi bentuk yang lebih nyata, proses ini disebut sebagai instansiasi. 
Itulah sebabnya objek disebut juga sebagai instance atau instance of the class.

class Mobil:
    # Atribut (variabel identitas)
    warna = "Merah"

mobil_1 = Mobil() #membuat objek baru dari clas mobil
print(mobil_1.warna) #bukti bahwa mobil_1 warnanya sama dengan mobil, yaitu merah struktur untuk memanggil atribut : print(nama_objek.nama_atribut)


- Atribut.
#merubah atribut bawaan (merah jd biru)

class Mobil:
    # Atribut
    warna = 'Merah'

mobil_1 = Mobil()
mobil_1.warna = "Biru"
print(mobil_1.warna)

a. atribut kelas (semua di wariskan,jika di ubah semua atribut objek berubah juga)

b. atribut objek/instance --> diperlukan class constructor dulu(sebuah fungsi khusus dalam python,untuk menentukan nilai awal atau kondisi awal dari suatu "kelas")
    class Mobil:
    def __init__(self):
        self.warna = 'Merah'  

Pada contoh di atas, kita membuat fungsi bernama "__init__" sebagai fungsi khusus untuk menjadi constructor. Selanjutnya, 
kita menggunakan parameter self, yakni sebuah kata kunci untuk merujuk pada objek yang sedang diproses saat ini.

class Mobil:
    # Atribut Instance
    def __init__(self):
        self.warna = 'Merah' #self merujuk ke class induk
        
mobil_1 = Mobil()
mobil_2 = Mobil()

print(mobil_1.warna)
print(mobil_2.warna)

# Mengubah atribut instance #di khususkan ke objek yang mau di ubah
mobil_1.warna = "Hitam"

# Menampilkan kembali atribut warna
print(mobil_1.warna)
print(mobil_2.warna)

"""
Output:
Merah
Merah
Hitam
Merah
"""
'''
class Mobil:
    # Atribut Instance
    def __init__(self):
        self.warna = 'Merah' #self merujuk ke class induk.  kita langsung menentukan nilai default terhadap suatu objek "merah"

mobil_1 = Mobil()
mobil_2 = Mobil()

print(mobil_1.warna)
print(mobil_2.warna)

# Mengubah atribut instance #di khususkan ke objek yang mau di ubah
mobil_1.warna = "biru donker"

# Menampilkan kembali atribut warna
print(mobil_1.warna)
print(mobil_2.warna)

#menambahkan parameter di constuction

class Mobil:
    def __init__(self,kecepatan,warna,merk):
        #atribut instance
        self.kecepatan = kecepatan
        self.warna = warna
        self.merk = merk

        #membuat objek mobil
mobil_1=Mobil(160,'kuning','toyota') #Parameter tambahan ini membuat kita perlu menggunakan argumen ketika memanggil kelas mobil "Mobil('Merah', 'DicodingCar', 160)".biasanya hanya mobil() sudah bisa

print(mobil_1.kecepatan)
print(mobil_1.warna)
print(mobil_1.merk)


'''Method (ada 3)
sebetulnya ini membuat fungsi didalam class/objek
Dekorator adalah fungsi dalam Python yang mengembalikan fungsi lain, biasanya diawali dengan sintaks "@" di awal
jadi panggil fungsi di dalam fungsi
def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dieksekusi.")
        func()
        print("Setelah fungsi dieksekusi.")
    return wrapper    #fungsi wrapper() bertindak sebagai "pembungkus" yang menambahkan perilaku sebelum dan setelah eksekusi dari fungsi func.

# Dekorasi fungsi dengan decorator. Untuk mendekorasi say_hello(), kita menggunakan simbol "@" diikuti dengan nama dekorator, yaitu @my_decorator sebelum mendefinisikan fungsi say_hello.
@my_decorator
def say_hello():
    print("Hello, world!")

# Memanggil fungsi yang sudah didekorasi
say_hello()

"""
Output:
Sebelum fungsi dieksekusi.
Hello, world!
Setelah fungsi dieksekusi.
"""
Dekorator sangat berguna untuk menambahkan fungsionalitas tambahan pada suatu fungsi atau metode tanpa harus mengubah kode asli dari fungsi tersebut.

-Metode dari object (object method).
  - adanya parameter self yg merujuk ke objek saat ini 

        class Mobil:
            def __init__(self, warna, merek, kecepatan):
                self.warna = warna
                self.merek = merek
                self.kecepatan = kecepatan

            def tambah_kecepatan(self):
                self.kecepatan += 10

        mobil_1 = Mobil("Merah", "DicodingCar", 160)
        print("Sebelum ditambahkan: ")
        print(mobil_1.kecepatan)

        mobil_1.tambah_kecepatan()        # Memanggil metode tambah_kecepatan.

        print("Setelah ditambahkan: ")
        print(mobil_1.kecepatan)
### bedanya ketika memanggil atribut & method = Ketika memanggil atribut, Anda cukup menyebutkan nama atribut tersebut tanpa ada tanda kurung “()”, contohnya “mobil_1.kecepatan”. 
# Namun untuk memanggil method, Anda harus menempatkan tanda kurung “()” setelahnya, contohnya “mobil_1.tambah_kecepatan()”.

mobil_1.tambah_kecepatan() setara dengan Mobil.tambah_kecepatan(mobil_1)
object method adalah metode yang melekat terhadap suatu objek dan menggunakan parameter self kita tidak bisa memanggil metode ini langsung melalui kelasnya

-Metode secara statis (static method).decorator.  independen dan tidak terikat pada instance kelas. (sama seperti fungsi pd umumnya cuma ddlm class)
    - dekorator @staticmethod tepat sebelum mendefinisikan fungsi atau metode (didlm class)
        class Mobil:
        def __init__(self, merek):
            self.merek = merek
        
        @staticmethod
        def intro_mobil():
            print("Ini adalah metode dari kelas Mobil")
            
    Mobil.intro_mobil()
    mobil_1 = Mobil("DicodingCar")
    mobil_1.intro_mobil()

    """
    Output:
    Ini adalah metode dari kelas Mobil

-Metode dari class (class method).decorator. ciri2 parameter cls yg merujuk pada class
    - penulisan @classmethod dan cls
    -  cls = Python akan secara otomatis menambahkan kelas tersebut sebagai argumen pertama.
        class Mobil:
            def __init__(self, merek):
                self.merek = merek

            @classmethod
            def intro_mobil(cls):
                print("Ini adalah metode dari kelas Mobil")
                
        Mobil.intro_mobil()
        mobil_1 = Mobil("DicodingCar")
        mobil_1.intro_mobil()

        """
        Output:
        Ini adalah metode dari kelas Mobil
        Ini adalah metode dari kelas Mobil
"""
'''
'''
Inheritance (Pewarisan) class

    class Mobil:
        def __init__(self, warna, merek, kecepatan):
            self.warna = warna
            self.merek = merek
            self.kecepatan = kecepatan
        
        def tambah_kecepatan(self):
            self.kecepatan += 10


    class MobilSport(Mobil):
        def turbo(self):
            self.kecepatan += 50

    # Kelas Mobil Dasar
    mobil_1 = Mobil("Merah", "DicodingCar", 160)
    print(mobil_1.kecepatan)

    # Kelas Mobil Sport
    mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
    print(mobil_sport_1.kecepatan)
    mobil_sport_1.turbo()
    print(mobil_sport_1.kecepatan)

    """
    Output:
    160
    160
    210
    """
'''
'''override 

    class Mobil:
        def __init__(self, warna, merek, kecepatan):
            self.warna = warna
            self.merek = merek
            self.kecepatan = kecepatan
        
        def tambah_kecepatan(self):     # tambah_kecepatan
            self.kecepatan += 10

    class MobilSport(Mobil):
        def turbo(self):
            self.kecepatan += 50
        
        def tambah_kecepatan(self):     # tambah_kecepatan
            self.kecepatan += 20

    # Kelas Mobil Sport
    mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
    print(mobil_sport_1.kecepatan)
    mobil_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
    print(mobil_sport_1.kecepatan)

    # Kelas Mobil Dasar (mobil dasar akan mengambil kecepatan pada kelas induk yang +10 bukan yg +20)
    mobil_1 = Mobil("Merah", "DicodingCar", 160)
    print(mobil_1.kecepatan)
    mobil_1.tambah_kecepatan()
    print(mobil_1.kecepatan)


    """
    Output:
    160
    180
    170
    """

Saat Anda menjalankan program, Python akan mencari nama metode dengan nama yang sesuai di kelas baru terlebih dahulu. 
Jika tidak ada, nama akan dicari di kelas induk.
'''
'''Super (memanggil metode induk)
    cara untuk kita ingin menggunakan metode atau atribut dari kelas induk, tetapi tidak ingin menuliskan ulang semua kode? Ini adalah tujuan dari adanya super

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10


class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50
    
    def tambah_kecepatan(self):
        super().tambah_kecepatan()
        print("Kecepatan Anda meningkat! Hati-Hati!")

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
mobil_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)

"""
Output:
Kecepatan Anda meningkat! Hati-hati!
170
"""
Pada metode ini, kita menggunakan "super()" untuk mengambil metode tambah_kecepatan yang berasal dari super class atau induknya, yaitu kelas Mobil. 
'''
'''pylint dan PEP8 (Python Enhancement Proposals) Pycodestyle untuk mencari error dan penulisan sesuai prosedur
yapf untuk rekomendasi penulisan code kita agar sesuai prosedur
'''
'''
saat membuat fungsi dan Anda menggabungkan anotasi dengan nilai parameter, sebaiknya tetap menggunakan spasi baik sebelum dan sesudah tanda sama dengan (=).

def LuasPersegiPanjang(panjang: int = 2, lebar: int = None):
    pass

Sekarang, kita masuk ke skenario baru. Jika pada saat membuat fungsi tanpa adanya anotasi bahwa parameternya menandakan keyword argumen atau nilai default, hindari penggunaan spasi di sekitar tanda sama dengan (=).

Yes:
def LuasPersegiPanjang(panjang=2, lebar=None):
    luas = panjang*lebar
    return luas
 
No:
def LuasPersegiPanjang(panjang = 2, lebar = None):
    luas = panjang*lebar
    return luas
'''
'''Style Guide Prinsip Penamaan pada Python
    - penamaan fungsi lebih ke penggunaan/fungsinya. cariJalan() lebih baik dibanding jalan()
    -Nama Kelas=Saat menamai kelas, gunakan CamelCase atau CapWords. Pastikan semua akronim (misal HTTP) ditulis keseluruhan dengan huruf besar.
    -Nama fungsi dan variabel= Gunakan underscore untuk memisahkan kata.
    -Nama Modul= Gunakan underscore untuk memisahkan kata.
    -Nama Konstanta= Gunakan huruf besar untuk menandakan bahwa nilai tidak dapat di ubah
    -Nama fungsi dan variabel yang mengandung angka= Gunakan underscore 
    -Nama fungsi dan variabel yang mengandung tanda baca= Gunakan underscore
    -Nama Exception = tamahkan error di belakangnya => DivideByZeroError
    -Nama Variabel Global= jika non publik pake garis bawah ddepannya biar kga ke import
    -Gunakan self sebagai argumen pertama jika Anda membuat instance method.
    -Gunakan cls sebagai argumen pertama ketika Anda membuat class method.
    -Jika nama argumen fungsi adalah reserved keyword, tambahkan garis bawah di akhir nama argumen.baca_
    -method dan variabel= Tambahkan garis bawah sebagai awalan untuk method non-publik dan variabel internal pada fungsi.
     Untuk menghindari kesamaan dengan subkelas, gunakan __dimulai_dua_garis_nama_method untuk memanggil proses yang tepat. Python menggabungkan nama modul dengan nama kelas. Misal ada suatu kelas bernama Foo, jika kelas Foo memiliki atribut __a, kita tidak dapat mengaksesnya melalui Foo.__a, tetapi Foo._Foo__a. Mulai dengan dua garis bawah hanya digunakan jika terjadi konflik dengan atribut di kelas atau subkelas lainnya.
     -konstanta hruf besar semua 'PI = 3,14'  atau  'TOTAL = 4.14213'.
     -jika ragu jadikan selalu atributnya non-publik,sebab lebih mudah dirubah ke publik lagi nantinya.

        class MyClass:
        def __init__(self):
            self._private_var = 42   # Variabel non publik dengan awalan satu garis bawah
            self._secret_list = [1, 2, 3]  # Variabel non publik lainnya

        def _private_method(self):
            print("Ini adalah method non publik")

        def public_method(self):
            print("Ini adalah method publik")
            self._private_method()  # Method publik dapat memanggil method non publik

    -Kategori lain dari atribut adalah "subclass API", umumnya disebut protected pada bahasa lain
    - Saat mendeklarasikan variabel/method tersebut, ikuti panduan Pythonic berikut. (publik & private)

        1. Atribut publik tidak menggunakan awalan garis bawah.
        2. Jika nama sebuah method/variabel publik sama dengan reserved keyword, tambahkan akhiran garis bawah. Hindari menyingkat atau mengurangi huruf.
        3. Pada data publik yang bersifat simpel, hindari nama yang terlalu panjang. Cukup dengan nama atribut sependek mungkin. Ingatlah bahwa pada masa depan Anda akan mungkin mengembangkan skema atau data ini sehingga nama sependek apa pun mungkin akan menguntungkan Anda.
        4. Jika Anda berniat untuk mewariskan atau membuat subclass dari kelas dan menginginkan sebuah variabel hanya digunakan di kelas utama saja, tambahkan awalan dua garis bawah. Ini akan memudahkan Anda karena Python mengenalinya sebagai konvensi kelas, untuk menghindari kemungkinan kesamaan nama atau implementasi.


'''
'''BNSP'''
def tukar_data(arr, i, j):
    """Fungsi untuk menukar posisi dua elemen dalam array"""
    arr[i], arr[j] = arr[j], arr[i] #bisa juga diganti dengan angka_urut

def bubble_sort(arr):
    """Prosedur pengurutan data menggunakan metode bubble sort"""
    n = len(arr) #Menyimpan panjang array arr ke dalam variabel n. Dibutuhkan untuk menentukan jumlah iterasi dalam pengurutan
    for i in range(n): #Loop pertama (outer loop/loopluar) menjalankan pengurutan sebanyak n iterasi
        for j in range(0, n-i-1): #Range dikurangi i karena setiap iterasi i menempatkan elemen terbesar ke posisi akhir, sehingga area yang perlu dibandingkan berkurang
            if arr[j] > arr[j+1]: #Membandingkan elemen saat ini (arr[j]) dengan elemen berikutnya (arr[j+1]).Jika elemen saat ini lebih besar, maka mereka akan ditukar.
                tukar_data(arr, j, j+1) #Fungsi tukar_data digunakan untuk menukar posisi elemen arr[j] dan arr[j+1].Misalnya, jika arr = [3, 2, 1], maka setelah tukar elemen:Langkah 1: [2, 3, 1]Langkah 2: [2, 1, 3]Langkah 3: [1, 2, 3]
    return arr #Setelah proses bubble sort selesai, fungsi mengembalikan array arr yang sudah terurut

def simpan_ke_file(arr, nama_file="hasil_pengurutan.txt"): #parameter menyimpan array di atas.  Nama file tempat menyimpan data. Jika tidak diberikan, secara default akan menggunakan "hasil_pengurutan.txt"
    """Fungsi untuk menyimpan hasil pengurutan ke file"""
    with open(nama_file, 'w') as file: #mode w = Membuka file untuk menulis.Jika file tidak ada, file akan dibuat secara otomatis.Jika file sudah ada, isinya akan dihapus (overwrite).jenis2 mode bisa di cari diinternet #with memastikan file ditutup secara otomatis setelah operasi selesai
        file.write("Hasil Pengurutan:\n") #menulis header "Hasil Pengurutan:" ke dalam file
        for angka in arr: #Melakukan iterasi untuk setiap elemen dalam array arr
            file.write(str(angka) + "\n") #Mengonversi angka menjadi string dan menambahkan karakter newline (\n) agar setiap angka berada di baris baru dalam file.

def baca_dari_file(nama_file="hasil_pengurutan.txt"):
    """Fungsi untuk membaca hasil pengurutan dari file""" # Membaca data dari file teks yang sudah disimpan sebelumnya
    try:
        with open(nama_file, 'r') as file: #Jika file tidak ditemukan
            return file.read() #Membaca seluruh isi file dan mengembalikannya sebagai string
    except FileNotFoundError:
        return "File tidak ditemukan!"

def main():
    while True:
        print("\nMenu Program Pengurutan:")
        print("1. Input dan Urutkan Angka")
        print("2. Tampilkan Hasil Pengurutan dari File")
        print("3. Keluar")
        
        pilihan = input("\nPilih menu [1/2/3]: ")
        
        if pilihan == "1":
            try:
                jumlah = int(input("Masukkan jumlah angka yang akan diinput: "))
                if jumlah <= 0:
                    print("Error: Jumlah angka harus lebih besar dari nol!")
                    continue
                angka = []
                
                for i in range(jumlah):
                    nilai = float(input(f"Masukkan angka ke-{i+1}: "))
                    angka.append(nilai)
                
                # Urutkan data
                hasil_urut = bubble_sort(angka)
                
                print("\nHasil pengurutan:")
                print(hasil_urut)
                
                # Simpan ke file
                simpan_ke_file(hasil_urut)
                print("Data berhasil disimpan ke file 'hasil_pengurutan.txt'")
                
            except ValueError:
                print("Error: Masukkan angka yang valid!")
                
        elif pilihan == "2":
            print("\nMembaca hasil pengurutan dari file:")
            hasil = baca_dari_file()
            print(hasil)
            
        elif pilihan == "3":
            print("Terima kasih telah menggunakan program ini!")
            break
            
        else:
            print("Pilihan tidak valid! Silakan pilih menu 1-3.")

if __name__ == "__main__": # di dalam block code main ini tidak akan dijalankan saat file diimpor. jadi yang bisa diimport hanya fungsi2 yg di luar main seperti (seperti bubble_sort, simpan_ke_file, atau baca_dari_file) 
    main()
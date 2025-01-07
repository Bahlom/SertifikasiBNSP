
def greeting(nama):
    """
    Prosedur untuk menampilkan sapaan kepada pengguna.
    
    Parameters:
        nama (str): Nama pengguna yang akan disapa.
    
    Returns:
        None
    """
    print("Halo!! " + nama + ", Selamat Datang Pada Aplikasi Penginputan dan Pengurutan Angka!")


def simpan_ke_file(arr, nama_file="hasil_pengurutan.txt"):
    """
    Fungsi untuk menyimpan hasil pengurutan ke dalam file.
    
    Parameters:
        arr (list): List berisi angka-angka yang sudah diurutkan.
        nama_file (str): Nama file tempat hasil pengurutan akan disimpan (default: 'hasil_pengurutan.txt').
    
    Returns:
        None
    """
    with open(nama_file, 'w') as file:
        file.write("Hasil Pengurutan:\n")
        for angka in arr:
            file.write(str(angka) + "\n")


def baca_dari_file(nama_file="hasil_pengurutan.txt"):
    """
    Fungsi untuk membaca hasil pengurutan dari file.
    
    Parameters:
        nama_file (str): Nama file yang akan dibaca (default: 'hasil_pengurutan.txt').
    
    Returns:
        str: Isi file jika berhasil dibaca.
        str: Pesan galat jika file tidak ditemukan.
    """
    try:
        with open(nama_file, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File tidak ditemukan!"


def main():
    """
    Fungsi utama untuk menjalankan program pengurutan angka. 
    Menampilkan menu, menerima input pengguna, dan memproses data berdasarkan pilihan pengguna.

    Menu Program:
        1. Input dan Urutkan Angka: Memasukkan angka, mengurutkan, dan menyimpannya ke file.
        2. Tampilkan Hasil Pengurutan dari File: Membaca hasil pengurutan dari file.
        3. Keluar: Mengakhiri program.
    
    Returns:
        None
    """
    name = input('Untuk Menjalankan Program Ini, Masukkan Nama Anda Terlebih dahulu:')
    # Memanggil prosedur greeting
    greeting(name)
    while True:
        print("\nMenu Program Pengurutan:")
        print("1. Input dan Urutkan Angka")
        print("2. Tampilkan Hasil Pengurutan dari File")
        print("3. Keluar")
        
        pilihan = input("\nPilih menu [1/2/3]: ")
        
        if pilihan == "1":
            try:
                jumlah = int(input("Masukkan jumlah angka yang akan diinput: "))
                
                angka = []
                
                for i in range(jumlah):
                    nilai = float(input(f"Masukkan angka ke-{i+1}: "))
                    angka.append(nilai)
                
                # Urutkan data
                hasil_urut = sorted(angka)
                
                print("\nHasil pengurutan:")
                print(hasil_urut)
                
                # Simpan ke file
                simpan_ke_file(hasil_urut)
                print("Data berhasil disimpan ke file 'hasil_pengurutan.txt'")
                
            except ValueError:
                print("Error: Masukkan angka yang valid! Jumlah angka harus lebih besar dari nol! tidak boleh selain angka!")
                
        elif pilihan == "2":
            print("\nMembaca hasil pengurutan dari file:")
            hasil = baca_dari_file()
            print(hasil)
            
        elif pilihan == "3":
            print("Terima kasih telah menggunakan program ini!")
            break
            
        else:
            print("Pilihan tidak valid! Silakan pilih menu 1-3.")


if __name__ == "__main__":
    main()
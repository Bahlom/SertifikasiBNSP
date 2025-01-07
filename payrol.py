from abc import ABC, abstractmethod #adalah bagian dari modul abc (Abstract Base Classes) di Python. Modul ini digunakan untuk membuat kelas abstrak, yang merupakan blueprint untuk kelas lain
from datetime import datetime

class Pegawai(ABC):
    def __init__(self, nip, nama, tahun_masuk, gaji_pokok):
        self._nip = nip #private atribut
        self.nama = nama
        self.tahun_masuk = tahun_masuk
        self.gaji_pokok = gaji_pokok
    
    @abstractmethod
    def hitung_gaji_akhir(self):
        pass
    
    def hitung_masa_kerja(self):
        tahun_sekarang = datetime.now().year
        return tahun_sekarang - self.tahun_masuk

class Satpam(Pegawai):
    def __init__(self, nip, nama, tahun_masuk, gaji_pokok, jam_lembur):
        super().__init__(nip, nama, tahun_masuk, gaji_pokok)
        self.jam_lembur = jam_lembur
        
    def hitung_honor_lembur(self):
        return self.jam_lembur * 20000
        
    def hitung_gaji_akhir(self):
        honor_lembur = self.hitung_honor_lembur()
        return self.gaji_pokok + honor_lembur

class Sales(Pegawai):
    def __init__(self, nip, nama, tahun_masuk, gaji_pokok, jumlah_pelanggan):
        super().__init__(nip, nama, tahun_masuk, gaji_pokok)
        self.jumlah_pelanggan = jumlah_pelanggan
        
    def hitung_komisi(self):
        return self.jumlah_pelanggan * 50000
        
    def hitung_gaji_akhir(self):
        komisi = self.hitung_komisi()
        return self.gaji_pokok + komisi

class Administrasi(Pegawai):
    def hitung_tunjangan(self):
        masa_kerja = self.hitung_masa_kerja()
        if masa_kerja >= 5:
            return self.gaji_pokok * 0.03
        elif masa_kerja >= 3:
            return self.gaji_pokok * 0.01
        return 0
        
    def hitung_gaji_akhir(self):
        tunjangan = self.hitung_tunjangan()
        return self.gaji_pokok + tunjangan

class Manajer(Pegawai):
    def __init__(self, nip, nama, tahun_masuk, gaji_pokok, persen_peningkatan_penjualan):
        super().__init__(nip, nama, tahun_masuk, gaji_pokok)
        self.persen_peningkatan_penjualan = persen_peningkatan_penjualan
        
    def hitung_bonus(self):
        if self.persen_peningkatan_penjualan > 10:
            return self.gaji_pokok * 0.10
        elif 6 <= self.persen_peningkatan_penjualan <= 10:
            return self.gaji_pokok * 0.05
        elif 1 <= self.persen_peningkatan_penjualan <= 5:
            return self.gaji_pokok * 0.02
        return 0
        
    def hitung_gaji_akhir(self):
        bonus = self.hitung_bonus()
        return self.gaji_pokok + bonus

class SistemPenggajian:
    def __init__(self):
        self.daftar_pegawai = []
        
    def tambah_pegawai(self, pegawai):
        self.daftar_pegawai.append(pegawai)
        
    def cetak_slip_gaji(self, pegawai):
        gaji_akhir = pegawai.hitung_gaji_akhir()
        
        print("\n=== SLIP GAJI ===")
        print(f"NIP: {pegawai._nip}")
        print(f"Nama: {pegawai.nama}")
        print(f"Tahun Masuk: {pegawai.tahun_masuk}")
        print(f"Gaji Pokok: Rp.{pegawai.gaji_pokok:,.2f}")
        
        if isinstance(pegawai, Satpam):
            honor_lembur = pegawai.hitung_honor_lembur()
            print(f"Honor Lembur ({pegawai.jam_lembur} jam): Rp.{honor_lembur:,.2f}")
            
        elif isinstance(pegawai, Sales):
            komisi = pegawai.hitung_komisi()
            print(f"Komisi ({pegawai.jumlah_pelanggan} pelanggan): Rp.{komisi:,.2f}")
            
        elif isinstance(pegawai, Administrasi):
            tunjangan = pegawai.hitung_tunjangan()
            print(f"Tunjangan: Rp.{tunjangan:,.2f}")
            
        elif isinstance(pegawai, Manajer):
            bonus = pegawai.hitung_bonus()
            print(f"Bonus (Peningkatan {pegawai.persen_peningkatan_penjualan}%): Rp.{bonus:,.2f}")
            
        print(f"Gaji Akhir: Rp.{gaji_akhir:,.2f}")
        print("================")

def main():
    sistem_penggajian = SistemPenggajian()
    
    while True:
        print("\nMenu:")
        print("1. Input Data Pegawai")
        print("2. Cetak Slip Gaji")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == "1":
            nip = input("NIP: ")
            nama = input("Nama: ")
            tahun_masuk = int(input("Tahun Masuk: "))
            gaji_pokok = float(input("Gaji Pokok: "))
            
            print("\nJabatan:")
            print("1. Satpam")
            print("2. Sales")
            print("3. Administrasi")
            print("4. Manajer")
            
            jabatan = input("Pilih jabatan (1-4): ")
            
            if jabatan == "1":
                jam_lembur = int(input("Jam Lembur: "))
                pegawai = Satpam(nip, nama, tahun_masuk, gaji_pokok, jam_lembur)
                
            elif jabatan == "2":
                jumlah_pelanggan = int(input("Jumlah Pelanggan: "))
                pegawai = Sales(nip, nama, tahun_masuk, gaji_pokok, jumlah_pelanggan)
                
            elif jabatan == "3":
                pegawai = Administrasi(nip, nama, tahun_masuk, gaji_pokok)
                
            elif jabatan == "4":
                persen_peningkatan = float(input("Persentase Peningkatan Penjualan: "))
                pegawai = Manajer(nip, nama, tahun_masuk, gaji_pokok, persen_peningkatan)
                
            else:
                print("Pilihan tidak valid!")
                continue
                
            sistem_penggajian.tambah_pegawai(pegawai)
            print("Data pegawai berhasil ditambahkan!")
            
        elif pilihan == "2":
            if not sistem_penggajian.daftar_pegawai:
                print("Belum ada data pegawai!")
                continue
                
            print("\nDaftar Pegawai:")
            for i, pgw in enumerate(sistem_penggajian.daftar_pegawai):
                print(f"{i+1}. {pgw.nama} ({pgw._nip})")
                
            idx = int(input("Pilih nomor pegawai: ")) - 1
            if 0 <= idx < len(sistem_penggajian.daftar_pegawai):
                sistem_penggajian.cetak_slip_gaji(sistem_penggajian.daftar_pegawai[idx])
            else:
                print("Nomor pegawai tidak valid!")
                
        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem penggajian!")
            break
            
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
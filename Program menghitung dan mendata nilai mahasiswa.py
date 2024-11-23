# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas):
    return (0.3 * nilai_tugas) + (0.35 * nilai_uts) + (0.35 * nilai_uas)

# Dictionary untuk menyimpan data mahasiswa
data_mahasiswa = {}

# Fungsi untuk menampilkan menu utama
def menu_utama():
    print("\nMenu Utama:")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("6. Keluar")
    pilihan = input("Pilih menu (1-6): ")
    return pilihan

# Fungsi untuk menambah data mahasiswa
def tambah_data():
    nama = input("Masukkan nama: ")
    nim = input("Masukkan NIM: ")
    nilai_tugas = float(input("Masukkan nilai tugas: "))
    nilai_uts = float(input("Masukkan nilai UTS: "))
    nilai_uas = float(input("Masukkan nilai UAS: "))
    
    nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)
    data_mahasiswa[nim] = {
        "nama": nama,
        "nilai_tugas": nilai_tugas,
        "nilai_uts": nilai_uts,
        "nilai_uas": nilai_uas,
        "nilai_akhir": nilai_akhir
    }
    print("Data berhasil ditambahkan.")

# Fungsi untuk mengubah data mahasiswa
def ubah_data():
    nim = input("Masukkan NIM mahasiswa yang akan diubah: ")
    if nim in data_mahasiswa:
        nama = input("Masukkan nama baru: ")
        nilai_tugas = float(input("Masukkan nilai tugas baru: "))
        nilai_uts = float(input("Masukkan nilai UTS baru: "))
        nilai_uas = float(input("Masukkan nilai UAS baru: "))
        
        nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)
        data_mahasiswa[nim] = {
            "nama": nama,
            "nilai_tugas": nilai_tugas,
            "nilai_uts": nilai_uts,
            "nilai_uas": nilai_uas,
            "nilai_akhir": nilai_akhir
        }
        print("Data berhasil diubah.")
    else:
        print("Data tidak ditemukan.")

# Fungsi untuk menghapus data mahasiswa
def hapus_data():
    nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
    if nim in data_mahasiswa:
        del data_mahasiswa[nim]
        print("Data berhasil dihapus.")
    else:
        print("Data tidak ditemukan.")

# Fungsi untuk menampilkan data mahasiswa
def tampilkan_data():
    print("\nDaftar Data Mahasiswa:")
    print("==========================================================================================")
    print("| No | Nama                      | NIM       | Tugas | UTS   | UAS   | Akhir             |")
    print("==========================================================================================")
    
    if data_mahasiswa:
        for i, (nim, mahasiswa) in enumerate(data_mahasiswa.items(), start=1):
            print(f"| {i:>2} | {mahasiswa['nama']:<25} | {nim:<9} | {mahasiswa['nilai_tugas']:<5} | {mahasiswa['nilai_uts']:<5} | {mahasiswa['nilai_uas']:<5} | {mahasiswa['nilai_akhir']:<17.2f} |")
            print("==========================================================================================")
    else:
        print("|                             Belum ada data mahasiswa                                  |")
        print("==========================================================================================")

# Fungsi untuk mencari data mahasiswa
def cari_data():
    nim = input("Masukkan NIM mahasiswa yang akan dicari: ")
    if nim in data_mahasiswa:
        mahasiswa = data_mahasiswa[nim]
        print("\nData Mahasiswa:")
        print("=========================================")
        print(f"Nama         : {mahasiswa['nama']}")
        print(f"NIM          : {nim}")
        print(f"Nilai Tugas  : {mahasiswa['nilai_tugas']}")
        print(f"Nilai UTS    : {mahasiswa['nilai_uts']}")
        print(f"Nilai UAS    : {mahasiswa['nilai_uas']}")
        print(f"Nilai Akhir  : {mahasiswa['nilai_akhir']:.2f}")
        print("=========================================")
    else:
        print("Data tidak ditemukan.")

# Loop utama untuk menampilkan menu dan memproses pilihan
while True:
    pilihan = menu_utama()
    
    if pilihan == '1':
        tambah_data()
    elif pilihan == '2':
        ubah_data()
    elif pilihan == '3':
        hapus_data()
    elif pilihan == '4':
        tampilkan_data()
    elif pilihan == '5':
        cari_data()
    elif pilihan == '6':
        print("Keluar dari program. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

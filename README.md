# Praktikum-5

Nama : Rifqi Maulana

NIM : 312410529

Kelas : TI.24.A.5

# Penjelasan program sederhana tabel data mahasiswa

## Flowchart program :

![Image](https://github.com/Shikilukeki/Foto/blob/main/Flowchart%20mendata%20mahasiswa.png?raw=true)

## Penjelasan :

```python
def hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas):
    return (0.3 * nilai_tugas) + (0.35 * nilai_uts) + (0.35 * nilai_uas)

```
Fungsi utama untuk menghitung nilai akhir mahasiswa berdasarkan bobot nilai tugas, UTS, dan UAS.

```python
data_mahasiswa = {}

```
Dictionary untuk menyimpan data mahasiswa

```python
def menu_utama():
    print("Program mendata mahasiswa")
    pilihan = input("[(t)ambah data, (u)bah data, (h)apus data, (c)ari data, (l)ihat data, (k)eluar] : ")
    return pilihan
```
Fungsi untuk menapilkan menu utama, pilihan operasi, dan menerima inputan operasi yang akan digunakan pengguna

```python
def tambah_data():
    while True:
        try:
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
            break
        except ValueError:
            print("Input tidak valid. Silakan coba lagi.")

```
Fungsi yang digunakan untuk menyimpan data baru mahasiwa yang diinputkan keadalam dictionary ```data_mahasiswa```

```python
def ubah_data():
    nim = input("Masukkan NIM mahasiswa yang akan diubah: ")
    if nim in data_mahasiswa:
        while True:
            try:
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
                break
            except ValueError:
                print("Input tidak valid. Silakan coba lagi.")
    else:
        print("Data tidak ditemukan.")
```
Fungsi yang digunakan untuk mengubah / menggantikan data mahasiswa yang sudah ada

```python
def hapus_data():
    nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
    if nim in data_mahasiswa:
        del data_mahasiswa[nim]
        print("Data berhasil dihapus.")
    else:
        print("Data tidak ditemukan.")
```
Fungsi yang berfungsi mencari data mahasiwa berdasarkan NIM 

```python
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
```
Fungsi yang menampilkan data mahsiswa berbentuk tabel

```python
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
```
Fungsi untuk mencari data mahasiswa

```python
while True:
    pilihan = menu_utama()
    
    if pilihan == 't':
        tambah_data()
    elif pilihan == 'u':
        ubah_data()
    elif pilihan == 'h':
        hapus_data()
    elif pilihan == 'l':
        tampilkan_data()
    elif pilihan == 'c':
        cari_data()
    elif pilihan == 'k':
        print("Keluar dari program. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
```

Loop untuk menampilkan menu utama dan pemilihan hingga pengguna memilih keluar (memasukan pilihan 6)

## Contoh hasil eksekusi program :

### Contoh eksekusi untuk menampilkan data dan menambahkan data baru mahasiswa:
![Image](https://github.com/Shikilukeki/Foto/blob/main/Tambah%20dan%20Lihat%20data%20mahasiswa.png?raw=true)

### Contoh hasil eksekusi untuk mengubah data mahasiswa:
![Image]()

### Contoh eksekusi untuk menghapus data mahasiswa:
![Image]()

### Contoh eksekusi untuk mencari data mahasiswa:
![Image]()

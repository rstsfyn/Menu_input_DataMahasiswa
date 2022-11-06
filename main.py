import datetime
x=datetime.datetime.now()

data=[]
#Bagian Input Data MAhasiswa
def inputDataMahasiswa():
    global data
    inputNim = int(input("Masukan NIM mahasiswa: "))
    inputNama = str(input("Masukan Nama mahasiswa: "))
    inputNilaiAgama = int(input("Masukan Nilai Agama: "))
    inputNilaiMatematika = int(input("Masukan Nilai Matematika: "))
    inputNilaiAlpro = int(input("Masukan Nilai Algoritma Pemrogtraman: "))
    dataBaru = []
    dataBaru.append(inputNim)
    dataBaru.append(inputNama)
    dataBaru.append(inputNilaiAgama)
    dataBaru.append(inputNilaiMatematika)
    dataBaru.append(inputNilaiAlpro)
    dataBaru.append(x)
    data.append(dataBaru)

#Bagian Tampil Semua Data Mahasiswa
def tampilSemuaDataMahsiswa():
    global data
    for i in data:
        print(i)

#Bagian Tampil Data NIM
def tampilDataNim():
    global data
    for i in data:
        print(i[0])

#Bagian Tampil Data Nama
def tampilDataNama():
    global data
    for i in data:
        print(i[1])

#Bagian Tampil Data Nilai
def tampilDataNilai():
    global data
    for i in data:
        print(i[2:])

#Bagian Cari Data Dengan NIM
def cariDataDenganNim():
    global data
    cariData = int(input("Masukan NIM untuk mencari Data: "))
    for i in data:
        if i[0] == cariData:
            print(i)
            break
        else:
            print("Data Not Found")

#Bagian Cari Data Dengan Nama
def cariDataDenganNama():
    global data 
    cariData = str(input("Masukan Nama Untuk Mencari Data: "))
    for i in data:
        if i[1] == cariData:
            print(i)
            break
        else:
            print("Daata Not Found")

#Bagian Cari Nilai Dengan NIM(tampil Nama Dan Nilai)
def cariNilaiDenganNim():
    global data
    cariData = int(input("Masukan NIM untuk mencari Nilai: "))
    for i in data:
        if i[0] == cariData:
            print(i[1:])
            break
        else:
            print("Data Not Found")

#Bagian Delete Data Dengan NIM
def deleteDataDenganNim():
    global data
    cariData = int(input("Masukan NIM untuk Menghaous Data: "))
    for i in data:
        if i[0] == cariData:
            data.remove(i)
            print(data)
            break
        else:
            print("Data Not Found")

#Bagian Edit Data Nama
def editDataNama():
    global data
    cariData = str(input("Masukan Nama untuk diubah: "))
    for i in data:
        if i[1] == cariData:
            ubahData = int(input("Masukan Index Untuk mengubah data:"))
            i[ubahData] = str(input("Masukan Nama Baru: "))
            print(i)
            break
        else:
            print("Data Not Found")

#Bagian Pilihan Menu
while True:             
    print("="*25)
    print("=======MENU UTAMA========")
    print("""
        1. Input Data Mahasiswa
        2. Tampil Semua Data 
        3. Tampil Data NIM
        4. Tampil Data Nama
        5. Tampil Data Nilai
        6. Cari Data Dengan NIM
        7. Cari Data Dengan Nama
        8. Cari Nilai Dengan NIM
        9. Delete Data Dengan NIM
        10. Edit Data Nama
        11. Exit
        """)
    print("="*25)
    pilihan = int(input("Masukan Nomor Untuk Memilih Menu: "))
    if pilihan == 1:
        inputDataMahasiswa()
        while True:
            ulang = input("Apakah Ingin Memasukan Data Lagi? [y/t]: ")
            if ulang == "t":
                break
            elif ulang == "y":
                continue
            else: 
                print("Tidak ada Pilihan")
                break
    elif pilihan == 2:
        tampilSemuaDataMahsiswa()
    elif pilihan == 3:
        tampilDataNim()
    elif pilihan == 4:
        tampilDataNama()
    elif pilihan == 5:
        tampilDataNilai()
    elif pilihan == 6:
        cariDataDenganNim()
    elif pilihan == 7:
        cariDataDenganNama()
    elif pilihan == 8:
        cariNilaiDenganNim()
    elif pilihan == 9:
        deleteDataDenganNim()
    elif pilihan == 10:
        editDataNama()
    else:
        print("Terimakasih Telah Menggunakan Menu ini")
        break
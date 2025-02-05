### LIST BARANG DI GUDANG
from tabulate import tabulate
data_logistik = [
{'Kode Barang':1,'Nama Barang':'Susu Kental Manis'     ,'Satuan':'Kaleng' ,'Barang Keluar':0,'Barang Masuk':5,'Stock Barang':5},
{'Kode Barang':2,'Nama Barang':'Susu UHT'              ,'Satuan':'Dus'    ,'Barang Keluar':0,'Barang Masuk':5,'Stock Barang':5},
{'Kode Barang':3,'Nama Barang':'Boba'                  ,'Satuan':'Bungkus','Barang Keluar':0,'Barang Masuk':5,'Stock Barang':5},
{'Kode Barang':4,'Nama Barang':'Susu Bubuk Varian Rasa','Satuan':'Bungkus','Barang Keluar':0,'Barang Masuk':5,'Stock Barang':5},
{'Kode Barang':5,'Nama Barang':'Cheese Cream'          ,'Satuan':'Bungkus','Barang Keluar':0,'Barang Masuk':5,'Stock Barang':5}
]

def main():

  print('''
        ========= KAMSIA BOBA GEMPOL SARI =========

        --------- Sistem Informasi Gudang ---------
        
          1. Menampilkan Daftar Barang
          2. Menambahkan Daftar Barang
          3. Memperbaharui Daftar Barang
          4. Menghapus Daftar Barang
          5. Keluar
        ''')

def read_data ():
    print('''
          ----------Menampilkan Daftar Barang----------
            1. Tampilkan Seluruh Daftar Barang
            2. Tampilkan Data Barang
            3. Mencari Data Tertentu
            4. Kembali ke Menu
          ''')

# MENAMPILKAN SELURUH DATA 
    read_data = input('Silahkan Pilih Menu Menampilkan Daftar Barang : ')
    if read_data.isdigit():
        if read_data == '1' :
            header = data_logistik[0].keys()
            rows = [x.values() for x in data_logistik]
            print('\n',tabulate(rows, header))
            print('\nDaftar Barang Berhasil Ditampilkan.\n')

# MENAMPILKAN SATU ROW DATA 
        elif read_data == '2':
            read_data1 = input('\nMasukkan Kode Barang : ')
            if read_data1.isdigit():            
                read_data1 = int(read_data1)
                i = read_data1 - 1
                if read_data1 > len(data_logistik) :
                    print('\nKode Barang Tidak Tersedia.')
                elif i != 0 :
                    headers = data_logistik[i].keys()
                    rows = [x.values() for x in data_logistik[i:i+1]]
                    print('\n',tabulate(rows,headers))
                elif i == 0 :
                    headers = data_logistik[i].keys()
                    rows = [x.values() for x in data_logistik[0:1]]
                    print('\n',tabulate(rows,headers))
                print('\nData Barang Berhasil Ditampilkan.\n')
            else:
                print('\nMasukkan Inputan yang Benar')

# MENCARI DATA TERTENTU
        elif read_data == '3' :
            read_data2 = input('\nMasukkan Kode Barang : ')
            read_data3 = input('\nMasukkan Kata Kunci : ')
            if read_data2.isdigit():
                read_data2 = int(read_data2)
                i_2 = read_data2 - 1 
                if read_data2 > len(data_logistik) :
                    print('\nKode Barang Tidak Tersedia.')
                elif read_data3 in data_logistik[i_2] :
                    nilai = data_logistik[i_2][read_data3]
                    print(f'\nData {read_data3} dengan Kode Barang {read_data2} = {nilai}')
                else :
                    print('\nData Tidak Tersedia')
            else :
                print('\nMasukkan Inputan yang Benar')
        else :
            print('\nMasukkan Inputan yang Benar')
    else:
        print('\nMasukkan Inputan yang Benar')

def create_data ():
    print('''
        ----------Menambahkan Daftar barang----------
          1. Tambah Daftar Barang
          2. Kembali ke Menu 
        ''')

# MENAMBAH DAFTAR BARANG
    create_data = input('Silahkan Pilih Menu Menambahkan Daftar Barang : ')
    if create_data.isdigit():
        if create_data == '1' :
            kode_barang = input('\nMasukkan Kode Barang : ')
            nama_barang = input('Masukkan Nama Barang : ')
            if kode_barang.isdigit():
                kode_barang = int(kode_barang)
                for i in data_logistik :
                    if kode_barang < len(data_logistik) :
                        if i == data_logistik[(kode_barang-1)] :
                            from tabulate import tabulate
                            headers = data_logistik[0].keys()
                            rows = [x.values() for x in data_logistik]
                            print('\n',tabulate(rows,headers))
                            # print(data_logistik[(kode_barang-1)])
                            print('\nData Sudah Ada.')
                            break
                    else :
                        satuan = input('Masukkan Satuan : ')
                        if satuan.isalpha():
                            barang_masuk = input('Masukkan Jumlah Barang Masuk : ')
                            if barang_masuk.isdigit():
                                barang_keluar = input('Masukkan Jumlah Barang Keluar : ')
                                if barang_keluar.isdigit():
                                    stock_barang = input('Masukkan Stock Barang : ')                      
                                    if stock_barang.isdigit():
                                        certain = input('Apakah Data Akan Disimpan?(Y/N) : ').lower()
                                    else:
                                        print('Masukkan Inputan yang Benar')
                                else:
                                    print('Masukkan Inputan yang Benar')
                            else:
                                print('Masukkan Inputan yang Benar')
                        else:
                            print('Masukkan Inputan yang Benar')                                 
                        
                        if certain.isalpha():
                            if certain == 'y':
                                barang_masuk = int(barang_masuk)
                                barang_keluar = int(barang_keluar)
                                stock_barang = int(stock_barang)
                                data_logistik.extend([{'Kode Barang':kode_barang,'Nama Barang':nama_barang,'Satuan':satuan,'Barang Keluar':barang_keluar,'Barang Masuk':barang_masuk,'Stock Barang':stock_barang}])
                                header = data_logistik[0].keys()
                                rows = [x.values() for x in data_logistik]
                                print('\n',tabulate(rows, header))
                                print('\nData Berhasil Disimpan.\n')
                                break
                            elif certain == 'n':
                                print('\nData Tidak Jadi Disimpan.')
                                break
                        else:
                            print('\nMasukkan Inputan yang Benar')
            else:
                print('\nMasukkan Inputan yang Benar')
    else:
        print('\nMasukkan Inputan yang Benar')

def update_data ():
    print('''
        ----------Memperbaharui Daftar barang----------
          1. Perbaharui Daftar Barang
          2. Edit Data Barang
          3. Kembali ke Menu
        ''')

# MEMPERBAHARUI DAFTAR SELURUH BARANG
    update_data = input('Silahkan Pilih Menu Memperbaharui Daftar Barang : ')
    if update_data.isdigit():
        if update_data == '1' :
            kode_barang1 = input('\nMasukkan Kode Barang : ')
            if kode_barang1.isdigit():
                kode_barang1 = int(kode_barang1)
                for i in data_logistik:
                    if kode_barang1 > len(data_logistik):
                        print('\nData Tidak Ada.')
                        break
                    if i == data_logistik[(kode_barang1-1)] :
                        print(data_logistik[(kode_barang1-1)])
                        certain1 = input('\nApakah Anda Akan Memperbaharui Data Tersebut?(Y/N) : ').lower()
                        if certain1 == 'y':
                            KB = input('\nSilahkan Perbaharui Kode Barang :')
                            data_logistik[kode_barang1-1]['Kode Barang'] = KB
                            if KB.isdigit():
                                NB = input('\nSilahkan Perbaharui Nama Barang :')
                                data_logistik[kode_barang1-1]['Nama Barang'] = NB
                                if NB.isalpha():
                                    S = input('\nSilahkan Perbaharui Satuan :')                                   
                                    data_logistik[kode_barang1-1]['Satuan'] = S
                                    if S.isalpha():
                                        BM = input('\nSilahkan Perbaharui Barang Masuk :')                                                                                                                                      
                                        data_logistik[kode_barang1-1]['Barang Masuk'] = BM                                        
                                        if BM.isdigit():
                                            BK = input('\nSilahkan Perbaharui Barang Keluar :')                                          
                                            data_logistik[kode_barang1-1]['Barang Keluar'] = BK
                                            BM = int(BM)
                                            BK = int(BK)
                                            BM1 = int(data_logistik[kode_barang1-1]['Barang Masuk'])
                                            BK1 = int(data_logistik[kode_barang1-1]['Barang Keluar'])
                                            data_logistik[kode_barang1-1]['Stock Barang'] = BM - BK1               
                                            data_logistik[kode_barang1-1]['Stock Barang'] = BM1 - BK
                                            print('\nData Berhasil Diperbaharui.')
                                        else:
                                            print('Masukkan Inputan yang Benar')
                                    else:
                                        print('Masukkan Inputan yang Benar')
                                else:
                                    print('Masukkan Inputan yang Benar') 
                            else:
                                print('Masukkan Inputan yang Benar')                                                       
                        elif certain1 == 'n':
                            print('\nData Tidak Jadi Diperbaharui.')
                        else:
                            print('Masukkan Inputan yang Benar')
            else:
                print('Masukkan Inputan yang Benar') 

# EDIT DATA BARANG       
        if update_data == '2' :
            kode_barang2 = input('\nMasukkan Kode Barang : ')
            if kode_barang2.isdigit():
                kode_barang2 = int(kode_barang2)
                for i in data_logistik:
                    if kode_barang2 > len(data_logistik):
                        print('\nData Tidak Ada.')
                        break
                    if i == data_logistik[(kode_barang2-1)] :
                        print(data_logistik[(kode_barang2-1)])
                        certain3 = input('\nApakah Anda Akan Memperbaharui Data Tersebut?(Y/N) : ').lower()
                        if certain3 == 'y':
                            print('''
                                    Pilih Data yang Akan Diperbaharui :
                                  
                                        1. Kode Barang
                                        2. Nama Barang
                                        3. Satuan
                                        4. Barang Masuk
                                        5. Barang Keluar
                                        
                                ''')
                            certain4 = input('\nMasukkan Data Yang Akan Anda Perbaharui : ')
                            if certain4.isdigit():
                                if certain4 == '1':
                                    data_logistik[kode_barang2-1]['Kode Barang'] = input('\nSilahkan Perbaharui Kode Barang :') 
                                    print('\nData Berhasil Diperbaharui.')
                                elif certain4 == '2':
                                    data_logistik[kode_barang2-1]['Nama Barang'] = input('\nSilahkan Perbaharui Nama Barang :') 
                                    print('\nData Berhasil Diperbaharui.')
                                elif certain4 == '3':
                                    data_logistik[kode_barang2-1]['Satuan'] = input('\nSilahkan Perbaharui Satuan :') 
                                    print('\nData Berhasil Diperbaharui.')                                                           
                                elif certain4 == '4':
                                    data_logistik[kode_barang2-1]['Barang Masuk'] = int(input(f'\nSilahkan Perbaharui Barang Masuk :'))                 
                                    data_logistik[kode_barang2-1]['Stock Barang'] = data_logistik[kode_barang2-1]['Barang Masuk'] - data_logistik[kode_barang2-1]['Barang Keluar']
                                    print('\nData Berhasil Diperbaharui.')
                                elif certain4 == '5':
                                    data_logistik[kode_barang2-1]['Barang Keluar'] = int(input(f'\nSilahkan Perbaharui Barang Keluar :'))                  
                                    data_logistik[kode_barang2-1]['Stock Barang'] = data_logistik[kode_barang2-1]['Barang Masuk'] - data_logistik[kode_barang2-1]['Barang Keluar']
                                    print('\nData Berhasil Diperbaharui.')                                                             
                            else:
                                print('Masukkan Inputan yang Benar')
                        elif certain3 == 'n':
                            print('\nData Tidak Jadi Diperbaharui.')
            else:
                print('Masukkan Inputan yang Benar')               
    else:
        print('Masukkan Inputan yang Benar')

def delete_data ():
    print('''
        ----------Menghapus Daftar barang----------
          1. Hapus Daftar Barang
          2. Kembali ke Menu
        ''')

# MENGHAPUS DAFTAR BARANG
    delete_data = input('\nSilahkan Pilih Menu Menghapus Daftar Barang : ')
    if delete_data.isdigit():
        if delete_data == '1' :
            kode_barang3 = input('\nMasukkan Kode Barang : ')
            if kode_barang3.isdigit():
                kode_barang3 = int(kode_barang3)
                if kode_barang3 > len(data_logistik):
                    print('\nData Tidak Ada.')

                for i in data_logistik:
                    if i == data_logistik[(kode_barang3-1)] :
                        print(data_logistik[(kode_barang3-1)])
                        certain5 = input('\nAnda Yakin Akan Menghapus Data Tersebut?(Y/N) : ').lower()
                        if certain5  == 'y':
                            del data_logistik[kode_barang3-1]
                            print('\nData Berhasil Dihapus.')
                        elif certain5 == 'n':
                            print('\nData Tidak Jadi Dihapus.')
            else:
                print('Masukkan Inputan yang Benar')
    else:
        print('Masukkan Inputan yang Benar')

while True:
    main()
    main_menu = input('Silahkan Pilih Menu (1-5) : ')
    if main_menu.isdigit():
        if main_menu == '1':
            read_data()
        elif main_menu == '2':
            create_data()
        elif main_menu == '3':
            update_data()
        elif main_menu == '4':
            delete_data()
        elif main_menu == '5':
            break
    else:
        print('\nPilihan Menu Tidak Valid. \n\nSilahkan Coba Lagi.')
   
print('\nTerima kasih.\n')
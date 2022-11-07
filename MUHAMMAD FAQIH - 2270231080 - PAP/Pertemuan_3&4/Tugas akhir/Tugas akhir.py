data_product = {
    1:"Laptop",
    2:"Mouse ",
    3:"Monitor",
    4:"Charger"
}
daftar_harga = {
    1: 2000000,
    2: 50000,
    3: 600000,
    4: 30000
}

dict_trx = {}
daftar_metode_pembayaran = {
    1:"transfer Bank",
    2:"Virtual Account",
    3:"Cash on Dalivery",
    4:"Kartu Kredit"
}
print("\n")
print("===== Selamat Datang Di Toko Elektronik Faqihun =====")
print("\n")
print("=============== List Product =============")
for i in data_product:
    print("",i,"Product : ",
         data_product[i],"\t Harga  : ",daftar_harga[i])
print("\n")
pilih_id = int(input("Pilih Nomor Product : "))
jumlah_pesanan = int(input("Pilih Jumlah Pesanan : "))
if pilih_id in data_product :
    pilih_beli = input("Konfirmasi Pesanan ? (Iya/Tidak) : ")
    if pilih_beli == "Iya"or pilih_beli == "iya":
        nama_penerima    = input("Nama Penerima    : ")
        alamat_penerima  = input("Alamat Penerima  : ")
        telepon          = input("No Hp            : ")
        kurir_pengiriman = input("Kurir Pengiriman : ")
        dict_trx = {
            "Nama Penerima":nama_penerima,
            "Alamat Penerima":alamat_penerima,
            "No Hp":telepon,
            "Kurir Pengiriman":kurir_pengiriman,
            "Product id":data_product,
        }
    else:
        pass
    
    if len (dict_trx) > 0 :
        print("\n")
        print("============ Metode Pembayaran ===========")
    for i in daftar_metode_pembayaran:
        print("", i, "1Metode Pembayaran : ", daftar_metode_pembayaran[i])
    pilih_metode = int(input("Pilih Nomor Metode Pembayaran : "))
    Harga =(daftar_harga[pilih_id]*jumlah_pesanan)
    if pilih_metode in daftar_metode_pembayaran :
        print("Nama Penerima : ", dict_trx["Nama Penerima"])
        print("Alamat Penerima : ", dict_trx["Alamat Penerima"])
        print("No Hp : ", dict_trx["No Hp"])
        print("Kurir Pengiriman : ", dict_trx["Kurir Pengiriman"])
        print("Product : ", data_product[pilih_id])
        print("Harga : ", Harga)
        print("Metode Pembayaran : ", daftar_metode_pembayaran[pilih_metode])
        konfirmasi = input("Apakah Anda Yakin Ingin Melakukan Pembayaran? (iya/tidak) : ")
        if konfirmasi == "iya" or konfirmasi == "Iya":
            print("Anda Sudah Berhasil Melakukan Pembayaran")
            print("Terima Kasih Sudah Mengunjungin Toko Kami")
        else:
            pass
    else:
        print("Metode Pembayaran Tidak Tersedia")
else:
    print("product tidak tersedia")
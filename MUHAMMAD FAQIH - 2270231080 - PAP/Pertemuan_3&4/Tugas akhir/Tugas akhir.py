data_product = {
    1:"Laptop",
    2:"Mouse ",
    3:"Monitor",
    4:"Charger",
    5:"Keyboard"
}
daftar_harga = {
    1: 10000000,
    2: 50000,
    3: 600000,
    4: 30000,
    5: 50000
}

dict_trx = {}
daftar_metode_pembayaran = {
    1:"transfer Bank",
    2:"Virtual Account",
    3:"Cash on Dalivery",
    4:"Kartu Kredit",
    5:"E-Wallet"
}
import datetime
now = datetime.datetime.now()
delta= datetime.timedelta(microseconds=now.microsecond)
now -= delta

print("\n")
print("=========== Selamat Datang Di Toko Elektronik Faqihun ===========")
print("\n")
print("=============== List Product ====================================")
for i in data_product:
    print("",i,"Product : ",
         data_product[i],"\t Harga  : ",daftar_harga[i])
print("=================================================================")
print("\n")
print("=================================================================")
pilih_id = int(input("┃Pilih Nomor Product                         : "))
jumlah_pesanan = int(input("┃Pilih Jumlah Pesanan                        : "))
if pilih_id in data_product :
    pilih_beli = input("┃Konfirmasi Pesanan ? (Konfirmasi/Batalakan) : ")
    print("\n")
    if pilih_beli == "Konfirmasi"or pilih_beli == "konfirmasi":
        print("=================================================================")
        nama_penerima    = input("┃Nama Penerima    : ")
        alamat_penerima  = input("┃Alamat Penerima  : ")
        telepon          = input("┃No Hp            : ")
        kurir_pengiriman = input("┃Kurir Pengiriman : ")
        dict_trx = {
            "Nama Penerima":nama_penerima,
            "Alamat Penerima":alamat_penerima,
            "No Hp":telepon,
            "Kurir Pengiriman":kurir_pengiriman,
            "Product id":data_product,
            }
        if len (dict_trx) > 0 :
            print("\n")
            print("=============== Metode Pembayaran ===============================")
        for i in daftar_metode_pembayaran:
            print("", i, "Metode Pembayaran : ", daftar_metode_pembayaran[i])
        print("=================================================================")
        print("\n")
        print("=================================================================")
        pilih_metode = int(input("┃Pilih Nomor Metode Pembayaran : "))
        Harga =(daftar_harga[pilih_id]*jumlah_pesanan)
        if pilih_metode in daftar_metode_pembayaran :
            konfirmasi = input("┃Apakah Anda Yakin Ingin Melakukan Pembayaran? (iya/tidak) : ")
            if konfirmasi == "iya" or konfirmasi == "Iya":
                print("\n")
                print("=================================================================")
                print("Tanggal Pembelian : ", now)
                print("Nama Penerima     : ", dict_trx["Nama Penerima"])
                print("Alamat Penerima   : ", dict_trx["Alamat Penerima"])
                print("No Hp             : ", dict_trx["No Hp"])
                print("Kurir Pengiriman  : ", dict_trx["Kurir Pengiriman"])
                print("Product           : ", data_product[pilih_id])
                print("Harga Barang      : ", daftar_harga[pilih_id])
                print("Harga Total       : ", Harga)
                print("Metode Pembayaran : ", daftar_metode_pembayaran[pilih_metode])
                print("=================================================================")
                print("\n")
                print("-TERIMA KASIH SUDAH BERBELANJA DI TOKO KAMI-")
                print("\n")
            elif konfirmasi == "Tidak" or konfirmasi == "tidak":
                print("\n")
                print("-PEMBAYARAN DIBATALKAN-")
                print("\n")
            else:
                print("\n")
                print("-COBA LAGI-")
                pass
        else:
            print("\n")
            print("-METODE PEMBAYARAN TIDAK TERSEDIA !-")
            print("\n")
    elif pilih_beli == "Batalkan"or pilih_beli == "batalkan":
        print("-Pesanan Dibatalkan-")
        print("\n")
    else:
        print("\n")
        pass
else:
    print("\n")
    print("-PRODUCT TIDAK TERSEDIA !-")
    print("\n")
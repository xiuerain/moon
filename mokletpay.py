print ("\t\tLayanan Moklet pay")
print ("\n\n\t1) Uang\t\t2) Dompet")
pilihan=input ("\n\nMasukan pilihan anda: ")
if pilihan=="1":
    print ("\n\t\tUang")
    print ("Bayar vendor")
    print ("\tPilih metode transfer")
    print ("\n1. Transfer Ke Kartu Bank\nMasukkan kartu bank penerima untuk mentransfer ke akun bank mereka")
    print ("\n2. Transfer Ke Nomor Ponsel\nMasukkan nomor ponsel penerima untuk mentransfer ke Saldo Moklet pay mereka") 
    transfer=input ("\nMasukkan metode transfer yang dipilih: ")
    if transfer=="1":
        Data_Nama_kartu=input ("\nMasukkan nama penerima: ")
        Data_No_kartu=input ("Masukkan nomor kartu kredit penerima: ")
        Bank=input ("Masukkan Bank Penerima: ")
        data_jumlah=input ("Masukkan jumlah uang yang ingin ditransfer: ")
        print ("\nSelanjutnya")
        print ("\n`\t1. Yes\t2. No")
        data_option=input ("Pilih yang di inginkan: ")
        if data_option=="1":
            print ("\n\tRp.",data_jumlah)
            print ("\n\tTransfer Berhasil")
            a= 1000000
            total= int(a)-int(data_jumlah)
            print ("\tSaldo anda tersisa: ",total)
        if data_option=="2":
            print ("\n\tTransfer Gagal")
    if transfer=="2":
        print("Masukkan nomor ponsel penerima yang tertaut dengan akun untuk transfer ke Saldo Moklet pay mereka")
        data_nomor=input ("nomor ponsel: ")
        data_jumlah=input ("Masukkan jumlah uang yang ingin ditransfer: ")
        print ("\nSelanjutnya")
        print ("\n\t1. Yes\t2. No")
        data_option=input ("\nPilih yang di inginkan: ")
        if data_option=="1":
            print ("\n\tRp.",data_jumlah)
            a= 1000000
            total= int(a)-int(data_jumlah)
            print ("\n\tTransfer Berhasil")
        print ("\tSaldo anda tersisa: ",total)
        if data_option=="2":
            print ("\n\tTransfer Gagal")
if pilihan=="2":
    print ("\n\t\tDompet")
    print ("\nJumlah Saldo: 1.000.000,00")
    print ("\n\t\t\t1. Top up saldo")
    print ("\n\t\t\t2. Kembali ke menu utama")
    data=input ("Masukkan pilihan anda: ")
    if data=="1":
        print ("\nHarap ke agen seperti Indomoklet terdekat")
        print ("\tMasukkan nomor Moklet pay(sesuai dengan nomor hp) anda")
        print ("\n\tTop up anda sedang dalam pengecekkan, ini bisa memakan waktu 3 hari.\n\tHarap rajin memeriksa saldo Moklet anda")
    if data=="2":
        print ("Silahkan run ulang Moklet pay")
        
    


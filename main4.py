# Program konversi mata uang asing ke Rupiah (static kurs)
Ulang = 'y'
KursDict = {}

while Ulang == 'y':
    Perintah = input('Masukkan perintah (KURS atau CONV) : ')
    SplitPerintah = Perintah.split()

    if SplitPerintah[0] == 'KURS':
        KursDict[SplitPerintah[1]] = SplitPerintah[2]

        file = open('riwayat transaksi.txt', 'a')
        file.write(Perintah + '\n')
        file.close()

        print('Apakah anda ingin kembali?')
        Ulang = input('Jawaban (y/n) : ')
        print()

    elif SplitPerintah[0] == 'CONV':
        if SplitPerintah[1] in KursDict:
            Kurs = int(KursDict[SplitPerintah[1]])
            Nilai = int(SplitPerintah[2])
            print(f'Konversi {" ".join(SplitPerintah[1:])} ke Rupiah (IDR) adalah {Kurs*Nilai}')

            file = open('riwayat transaksi.txt', 'a')
            file.write(Perintah + '\n')
            file.close()

        else:
            print('Kurs tidak ada di dalam kamus!\n')

        print('Apakah anda ingin kembali?')
        Ulang = input('Jawaban (y/n) : ')
        print()

    else:
        print('Perintah tidak valid!\n')
        break

print('Program konversi selesai..')
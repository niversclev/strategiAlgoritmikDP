class Barang:
    def __init__(self, nama, berat, profit):
        self.nama = nama
        self.berat = int(berat)    
        self.profit = int(profit)


## Kamus data
# items: list of Barang yang merupakan parameter
# kapasitas: parameter yang merupakan kapasitas maksimum knapsack (int)
def knapsack(items, kapasitas):
    jumlahBarang = len(items)
    visualProses = []
    tabelProses = []
    
    # aku buat sebuah kolom yang isinya 0 (profit o dan hasil x juga 0)
    # ini kaya prses buat tabel manual di sisa kapasitas 0
    kolom0 = []
    solusi0 = [0] * jumlahBarang
    for i in range(kapasitas + 1):
        kolom0.append({'profit': 0, 'solusi': solusi0.copy()})
    tabelProses.append(kolom0)
    
    # sekarang aku buat tabel untuk setiap barang 
    # jadi nanti bertahap gitu barangnya
    for i in range(1, jumlahBarang+1, 1):
        barangSekarang = items[i-1]
        # ini buat output setiap tahap
        outputSekarang = {
            'barang': barangSekarang.nama[0],
            'berat': barangSekarang.berat,
            'profit': barangSekarang.profit,
            'tabel': []
        }
        
        kolomSekarang = []
        for j in range(0, kapasitas + 1, 1):
            # pilihan 1: kalau barangnya tidak dipilih
            dataTidakDipilih = tabelProses[i-1][j] # -> ini nunjukin kalo kt ambil data sebelumnya
            profitTidakDipilih = dataTidakDipilih['profit']
            profitJikaAmbil = -1
            if (barangSekarang.berat <= j):
                # pilihan 2: kalau barangnya dipilih
                sisaKapasitas = j - barangSekarang.berat
                dataDipilih = tabelProses[i-1][sisaKapasitas]
                profitJikaAmbil = dataDipilih['profit'] + barangSekarang.profit

            # ini sebenernya buat nentuin mana yang lebih baik
            if (profitJikaAmbil > profitTidakDipilih):
                profitTerbaik = profitJikaAmbil
                # kalau barangnya dipilih
                solusiTerbaik = dataDipilih['solusi'][:]
                solusiTerbaik[i-1] = 1 # barang ini 1 brarti (terbaik)
            else:
                # kalau barangnya ga dipilih
                profitTerbaik = profitTidakDipilih
                solusiTerbaik = dataTidakDipilih['solusi']
            #ok ini cara nyimpen data ke tabel
            kolomSekarang.append({'profit': profitTerbaik, 'solusi': solusiTerbaik})
        
            dataBarisVisualisasi = {
                'y': j,
                'f prev': profitTidakDipilih,
                'calculate': profitJikaAmbil if profitJikaAmbil != -1 else None,
                'f new': profitTerbaik,
                'solusi optimum': str(tuple(solusiTerbaik))
            }
            outputSekarang['tabel'].append(dataBarisVisualisasi)
        
        # simpan output setiap tahap
        tabelProses.append(kolomSekarang)
        visualProses.append(outputSekarang)
        
    # hasil akhir berarti
    hasilFinal = tabelProses[jumlahBarang][kapasitas]
    profitFinal = hasilFinal['profit']
    listSolusi = hasilFinal['solusi']
    beratFinal = sum(items[i].berat for i in range(jumlahBarang) if listSolusi[i] == 1)
    
    # print hasil akhir
    solusiFinal = {
        'komposisi': str(tuple(listSolusi)),
        'profit': profitFinal, 
        'berat': beratFinal,
    }
    
    return {   
        'visualisasi': visualProses,
        'solusiFinal': solusiFinal
    }

def display_terminal(hasil_lengkap):
    """
    Mencetak hasil lengkap ke terminal sesuai dengan struktur data
    yang dihasilkan oleh fungsi knapsack Anda.
    """
    print("=======================================================================")
    print("                VISUALISASI PROSES KNAPSACK DP                         ")
    print("=======================================================================")
    
    # Mengakses list 'visualisasi' dari dictionary hasil_lengkap
    # Sebelumnya: hasil_lengkap['visualisasi'] -> Sekarang: hasil_lengkap['visualisasi'] (Sama, sudah benar)
    for i, tahap in enumerate(hasil_lengkap['visualisasi']):
        
        # Mengakses nama, profit, dan berat barang dari dictionary 'tahap'
        # Sebelumnya: tahap['nama_barang'], tahap['profit_barang'], tahap['berat_barang']
        # Sekarang: tahap['barang'], tahap['profit'], tahap['berat']
        print(f"\n### TAHAP {i+1}: Mempertimbangkan Barang '{tahap['barang']}' (P:{tahap['profit']}, W:{tahap['berat']}) ###\n")
        
        # Header tabel, ini bisa tetap sama karena hanya teks
        header = f" {'y':<3} | {'f' + str(i) + '(y)':<8} | {'P+f' + str(i) + '(y-W)':<12} | {'f' + str(i+1) + '(y)':<8} | {'Solusi Optimum':<20}"
        print(header)
        print("-" * (len(header) + 2)) # Menambahkan sedikit padding
        
        # Mengakses list 'tabel' dari dictionary 'tahap'
        # Sebelumnya: tahap['tabel_tahap'] -> Sekarang: tahap['tabel']
        for baris in tahap['tabel']:
            
            # Mengakses setiap data dalam satu baris visualisasi
            # Sebelumnya: baris['f_prev'], baris['calc_if_taken'], baris['f_new'], baris['solusi_optimum']
            # Sekarang: baris['f prev'], baris['calculate'], baris['f new'], baris['solusi optimum']
            
            # Menangani jika nilai 'calculate' adalah None
            calc_value = str(baris['calculate']) if baris['calculate'] is not None else '-inf'

            print(f" {baris['y']:<3} | {baris['f prev']:<8} | {calc_value:<12} | {baris['f new']:<8} | {baris['solusi optimum']:<20}")

    print("\n=======================================================================")
    print("                               HASIL AKHIR                             ")
    print("=======================================================================")
    
    # Mengakses dictionary 'solusiFinal' dari hasil_lengkap
    # Sebelumnya: hasil_lengkap['solusi_akhir'] -> Sekarang: hasil_lengkap['solusiFinal']
    solusi_akhir = hasil_lengkap['solusiFinal']
    
    # Mengakses setiap data dari dictionary 'solusi_akhir'
    # Sebelumnya: solusi_akhir['komposisi'], solusi_akhir['total_profit'], solusi_akhir['total_berat']
    # Sekarang: solusi_akhir['komposisi'], solusi_akhir['profit'], solusi_akhir['berat']
    print(f"Komposisi Barang yang Diambil : {solusi_akhir['komposisi']}")
    print(f"Total Profit Maksimal         : {solusi_akhir['profit']}")
    print(f"Total Berat                   : {solusi_akhir['berat']}")
    print("=======================================================================\n")

def main():
    items = [
    Barang(nama='Barang A', berat=1, profit=60),
    Barang(nama='Barang B', berat=5, profit=100),
    Barang(nama='Barang C', berat=2, profit=50),
    # Barang(nama='Barang D', berat=3, profit=30),
    # Barang(nama='Barang E', berat=7, profit=120),
    # Barang(nama='Barang F', berat=15, profit=75),
    # Barang(nama='Barang G', berat=2, profit=100),
    # Barang(nama='Barang H', berat=5, profit=55),
    # Barang(nama='Barang I', berat=10, profit=80),
    # Barang(nama='Barang J', berat=9, profit=20),
]
    kapasitas = 5
    hasil = knapsack(items, kapasitas)
    display_terminal(hasil)
    # print(f"Nilai maksimum yang dapat diperoleh: {hasil}")
    
if __name__ == '__main__':
    main()


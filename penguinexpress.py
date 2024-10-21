import tabulate, datetime

## Data diperoleh dari https://github.com/benangmerah/wilayah/blob/master/datasources/daftar-nama-daerah.csv
## Koordinat disimpan dalam tuple: (longitude, langitude)
## Kabupaten Pangandaran tidak termasuk data yang dilampirkan dari URL, tetapi karena merupakan pemekaran Kabupaten Ciamis,
## Kabupaten Pangandaran menggunakan koordinat Kabupaten Ciamis.
## Digunakan untuk perhitungan biaya pengiriman.
## Note: Karena pengiriman hanya dilakukan di pulau Jawa, maka kota/kabupaten yang dimasukkan hanyalah kota/kabupaten di pulau Jawa.
koordinat_kota = {'Kab Banyuwangi': (114.3669444, -8.2186111),
 'Kab Madiun': (111.505483, -7.627753),
 'Kab Ponorogo': (111.466003, -7.867827),
 'Kab Magetan': (111.3381593, -7.6493413),
 'Kab Pacitan': (111.08769, -8.204614),
 'Kab Ngawi': (111.46193, -7.38993),
 'Kab Bangkalan': (112.7450068, -7.0306912),
 'Kab Kediri': (112.032356, -7.809356),
 'Kab Bondowoso': (113.813483, -7.917704),
 'Kab Blitar': (112.162762, -8.1014419),
 'Kab Trenggalek': (111.7166667, -8.05),
 'Kab Tulungagung': (111.9, -8.0666667),
 'Kab Nganjuk': (111.901808, -7.602932),
 'Kab Situbondo': (113.955605, -7.702534),
 'Kab Malang': (112.6884549, -8.0495643),
 'Kab Jember': (113.700302, -8.172357),
 'Kab Sumenep': (113.9060624, -6.9253999),
 'Kab Pasuruan': (108.8001936, -6.8623098),
 'Kab Pamekasan': (113.4666667, -7.1666667),
 'Kab Probolinggo': (113.210675, -7.753965),
 'Kab Lumajang': (113.226601, -8.137022),
 'Kab Bojonegoro': (124.4669566, 0.882681),
 'Kab Tuban': (115.1711298, -8.7493146),
 'Kab Lamongan': (109.3946794, -7.406153),
 'Kab Sidoarjo': (112.7173389, -7.4530278),
 'Kab Sampang': (109.2058436, -7.5782556),
 'Kab Mojokerto': (112.427027, -7.488075),
 'Kab Gresik': (112.6555, -7.15665),
 'Kab Jombang': (112.2264794, -7.5468395),
 'Kota Mojokerto': (112.4336111, -7.4722222),
 'Kota Surabaya': (112.734398, -7.289166),
 'Kota Madiun': (111.513702, -7.629714),
 'Kota Blitar': (112.15, -8.1),
 'Kota Malang': (112.626503, -7.981894),
 'Kota Batu': (112.5239, -7.8671),
 'Kota Pasuruan': (112.903297, -7.644872),
 'Kota Kediri': (112.011398, -7.816895),
 'Kota Probolinggo': (113.211502, -7.756928),
 'Kab Kepulauan Seribu': (106.5071982, -5.7985266),
 'Kota Jakarta Selatan': (106.807915, -6.332973),
 'Kota Jakarta Timur': (106.845172, -6.211544),
 'Kota Jakarta Pusat': (106.845172, -6.211544),
 'Kota Jakarta Barat': (106.845172, -6.211544),
 'Kota Jakarta Utara': (106.845172, -6.211544),
 'Kab Bogor': (106.8, -6.6),
 'Kab Sukabumi': (106.922203, -6.92405),
 'Kab Cianjur': (107.1307289, -6.8172531),
 'Kab Bandung': (107.6098111, -6.9147444),
 'Kab Garut': (107.908699, -7.227906),
 'Kab Tasikmalaya': (108.214104, -7.327954),
 'Kab Ciamis': (108.35, -7.3333333),
 'Kab Kuningan': (108.4833333, -6.9833333),
 'Kab Cirebon': (108.564003, -6.715534),
 'Kab Majalengka': (108.2258897, -6.8531026),
 'Kab Sumedang': (110.0330554, 0.6095949),
 'Kab Indramayu': (108.325104, -6.336315),
 'Kab Subang': (107.752403, -6.569361),
 'Kab Purwakarta': (107.4499404, -6.5386806),
 'Kab Karawang': (107.3375791, -6.3227303),
 'Kab Bekasi': (107.0, -6.2333333),
 'Kab Bandung Barat': (107.4321959, -6.8937121),
 'Kota Bogor': (106.8, -6.6),
 'Kota Sukabumi': (106.922203, -6.92405),
 'Kota Bandung': (107.6098111, -6.9147444),
 'Kota Cirebon': (108.564003, -6.715534),
 'Kota Bekasi': (107.0, -6.2333333),
 'Kota Depok': (106.83, -6.39),
 'Kota Cimahi': (107.5355, -6.880239),
 'Kota Tasikmalaya': (108.214104, -7.327954),
 'Kota Banjar': (108.5333333, -7.3666667),
 'Kab Cilacap': (109.0, -7.733333),
 'Kab Banyumas': (109.140438, -7.4832133),
 'Kab Purbalingga': (109.3638, -7.390747),
 'Kab Banjarnegara': (109.681396, -7.402706),
 'Kab Kebumen': (109.656502, -7.678682),
 'Kab Purworejo': (110.008003, -7.709731),
 'Kab Wonosobo': (109.899399, -7.362109),
 'Kab Magelang': (110.213799, -7.481253),
 'Kab Boyolali': (110.595901, -7.523819),
 'Kab Klaten': (110.595497, -7.711687),
 'Kab Sukoharjo': (110.8195292, -7.6808818),
 'Kab Wonogiri': (110.920601, -7.817782),
 'Kab Karanganyar': (110.9508333, -7.5961111),
 'Kab Sragen': (111.021301, -7.430229),
 'Kab Grobogan': (110.9625854, -7.0217194),
 'Kab Blora': (111.4166667, -6.95),
 'Kab Rembang': (111.345299, -6.71124),
 'Kab Pati': (111.038002, -6.751338),
 'Kab Kudus': (110.838203, -6.804087),
 'Kab Jepara': (110.6717, -6.5596059),
 'Kab Demak': (110.639297, -6.888115),
 'Kab Semarang': (110.4166667, -6.9666667),
 'Kab Temanggung': (110.174797, -7.316669),
 'Kab Kendal': (110.205597, -6.919686),
 'Kab Batang': (109.7234519, -6.8941111),
 'Kab Pekalongan': (109.669998, -6.882887),
 'Kab Pemalang': (109.377998, -6.884234),
 'Kab Tegal': (109.1333333, -6.8666667),
 'Kab Brebes': (109.05, -6.8833333),
 'Kota Magelang': (110.213799, -7.481253),
 'Kota Surakarta': (110.8166667, -7.5666667),
 'Kota Salatiga': (110.4729, -7.302328),
 'Kota Semarang': (110.4166667, -6.9666667),
 'Kota Pekalongan': (109.669998, -6.882887),
 'Kota Tegal': (109.1333333, -6.8666667),
 'Kab Kulon Progo': (110.1640846, -7.8266798),
 'Kab Bantul': (110.3341111, -7.8846111),
 'Kab Gunung Kidul': (110.6168921, -8.0305091),
 'Kota Yogyakarta': (110.368797, -7.797224),
 'Kab Pandeglang': (106.103897, -6.314835),
 'Kab Lebak': (106.2522143, -6.5643956),
 'Kab Tangerang': (106.6318889, -6.1783056),
 'Kab Serang': (106.150299, -6.12009),
 'Kota Tangerang': (106.6318889, -6.1783056),
 'Kota Cilegon': (106.040506, -6.0169825),
 'Kota Serang': (106.150299, -6.12009),
 'Kab Sleman': (110.335403, -7.716165),
 'Kota Tangerang Selatan': (106.7180556, -6.2888889),
 'Kab Pangandaran': (108.35, -7.3333333)}

today_date = datetime.datetime.now()
delta_time = [3, 5, 1, 0, 2, 0, 0] # Untuk tanggal pengiriman
delta_time = [datetime.timedelta(days=day) for day in delta_time]

date_format = "%Y-%m-%d" #Tahun-Bulan-Tanggal

id_pengiriman = [98, 101, 105, 107, 108, 109, 110] # Primary key; tidak diisi di awal; korespon dengan digit sesudah PE pada nomor resi; eg: PE150 -> id_pengiriman = 150 
delivery_date = ['2024-10-17', '2024-10-15', '2024-10-19', '2024-10-20', '2024-10-18', '2024-10-20', '2024-10-20'] # Tidak diisi di awal; Mohon ikuti format date_format
delivery_date = [datetime.datetime.strptime(date, date_format).date() for date in delivery_date]
nama_pengirim = ['Jojon', 'Mulyadi', 'Bang Tagor', '@bdglabsupplies','Chacha', '@bdglabsupplies', '@bdglabsupplies' ]
nomor_pengirim = ['08510004444', '08177788555', '08459988777', '08123456789', '08785566123', '08123456789', '08123456789']
alamat_tujuan = ['Jl. Dompyong, Kalimekar, Kec. Gebang, Kabupaten Cirebon', 'Sumenep, Jl. KH. Wahid Hasyim No.51, Pakalongan, Bangselok', 'Jl. Madukoro Raya No.3, Krobokan, Kec. Semarang Barat, Kota Semarang, Jawa Tengah', 'Jl. Ir. H. Djuanda No.14, Bogor', 'Jl. Mojopahit No.44-50, Kebonsari, Bulusidokare, Kec. Sidoarjo, Kabupaten Sidoarjo, 61214',  'Jl. Ir. H. Djuanda No.14, Bogor', 'Jl. Ir. H. Djuanda No.14, Bogor']
kota_tujuan = ['Kab Cirebon', 'Kab Sumenep', 'Kota Semarang', 'Kota Bogor', 'Kab Sidoarjo', 'Kota Bogor', 'Kota Bogor']
nama_penerima = ['Udin', 'Ucok', 'Ubing', 'Usep', 'Uty','Usep', 'Usep'] 
nomor_penerima = ['0814000777', '0820240024', '08564000700', '08112233456', '081820202222', '08112233456', '08112233456']
berat_barang = [1, 0, 2, 10, 1, 10, 10]
## Kode jenis_barang: 1: Document | 2: Food | 3: Clothing | 4: Electronics | 5: Fragile | 6: Others"
jenis_barang = [4, 1, 2, 5, 3, 5, 5]
biaya = [12000.0, 15000.0, 22000.0, 84000.0, 14000.0, 84000.0, 84000.0] # Tidak diisi di awal
status = ['IN WAREHOUSE', 'DELIVERED', 'ON-PROCESS', 'ON-PROCESS', 'ON-PROCESS', 'ON-PROCESS', 'ON-PROCESS'] # Tidak diisi di awal
# Sisanya wajib diisi

data_pengiriman = {'id': id_pengiriman,
                  'delivery_date': delivery_date,
                   'sender': nama_pengirim,
                   'sender_no': nomor_pengirim,
                   'address': alamat_tujuan,
                   'city': kota_tujuan,
                   'recipient': nama_penerima,
                   'recipient_no': nomor_penerima,
                   'weight': berat_barang,
                   'type': jenis_barang,
                   'cost': biaya,
                   'status': status}

continue_token = 'continue_loop'
kota_pengiriman = 'Kota Bandung'
kota_pengiriman = kota_pengiriman.title() ## Memastikan kota_pengiriman dalam titlecase jika kasusnya kota_pengiriman diedit secara manual
kata_sandi = None
panjang_maks_kolom = [4, 10, 10, 10, 10, 10, 8, 5, 4, 7, 10]
panjang_maks_kolom_konfirmasi_penambahan_data = [10, 10, 10, 10, 10, 10, 5, 4, 7]
price_per_distance = 527.29 # Dari trial and error
base_price = 7500



def find_index(lst, val):
    ## Cari indeks suatu list/tuple
    ## Return -1 kalau indeks tidak ditemukan
    for i in range(len(lst)):
        if lst[i] == val:
            return i
    return -1

def hitung_jarak(titik_1, titik_2):
    ## Taxicab distance antara dua titik
    jarak =  abs(titik_1[0] - titik_2[0]) + abs(titik_1[1] - titik_2[1])
    return jarak

def tarif_pengiriman(jarak, berat, price_per_distance, base_price):
    if berat <=1:
        faktor_berat = 1
    else:
        faktor_berat = berat
    tarif = round((price_per_distance*jarak + base_price)/1000,0) * 1000 * faktor_berat + 4000
    return tarif

def infinite_looper(func):
    ## Loop suatu fungsi hingga fungsi tsb. mengembalikan suatu value
    ## Note: loop selesai jika value sudah di-return (bisa None)
    ## Jika terjadi error, loop dimulai kembali
    def wrapper(*args, **kwargs):
        while True:
            try:
                ret_val = func(*args, **kwargs)
                if ret_val == continue_token: ## Kalau fungsi mengembalikan continue_token, ulangi iterasi
                    continue
                else:
                    return ret_val ## Keluar fungsi -> keluar loop
            except Exception as e:
                print(e) ## Terjadi error -> print pesan error dan ulangi iterasi
                
    return wrapper


### Fungsi di bawah ini digunakan untuk input features pada tabel data.
@infinite_looper
def input_id_pengiriman():
    ## Untuk penampilan data, pembuatan data, dan pembaharuan data
    id_data = int(input("Masukkan id pengiriman: "))
    return id_data

@infinite_looper
def input_berat_barang():
    berat_barang = int(input("Masukkan berat barang (kg): "))
    if berat_barang < 0 or berat_barang > 10:
        raise Exception("Error. Berat barang tidak bisa negatif atau lebih dari 10kg.")
    return berat_barang

@infinite_looper
def input_nonempty_string(pesan_input):
    ## Untuk validasi input nama, alamat, dan nomor telefon, karena kolom tersebut tidak boleh kosong
    ## Juga digunakan untuk pembuatan/pengubahan kode sandi
    val = input(pesan_input)
    if len(val) == 0:
        raise Exception("Error. Input tidak boleh kosong.")
    return val

def input_nama_pengirim():
    return input_nonempty_string("Masukkan nama pengirim: ")

def input_no_pengirim():
    return input_nonempty_string("Masukkan no. telefon pengirim: ")

def input_alamat_tujuan():
    return input_nonempty_string("Masukkan alamat tujuan: ")

def input_nama_penerima():
    return input_nonempty_string("Masukkan nama penerima: ")

def input_no_penerima():
    return input_nonempty_string("Masukkan no. telefon penerima: ")
    

@infinite_looper
def input_kota():
    kota = input("Masukkan kota/kabupaten: ").title()
    if kota not in koordinat_kota:
        raise Exception("Error. Daerah ini tidak ada dalam database.")
    return kota

@infinite_looper
def input_jenis_barang():
    print("Masukkan kode jenis barang (bilangan bulat dari 1-6): ")
    kode_jenis_barang = int(input("1: Document | 2: Food | 3: Clothing | 4: Electronics | 5: Fragile | 6: Others\n"))
    if kode_jenis_barang < 1 or kode_jenis_barang > 6:
        raise Exception("Error. Tolong masukkan bilangan bulat dari 1-6.")
    return kode_jenis_barang

map_status_pengiriman = {1: 'ON-PROCESS', 2:'DELIVERED', 3:'ON-HOLD',  4:'IN-WAREHOUSE', 5:'BAD ADDRESS'}


@infinite_looper
def input_status_pengiriman():
    ## Digunakan untuk update, bukan untuk create
    print("Masukkan kode jenis barang (bilangan bulat dari 1-5): ")
    kode_status_pengiriman = int(input("1: ON-PROCESS | 2: DELIVERED | 3: ON-HOLD | 4: IN WAREHOUSE | 5: BAD ADDRESS\n"))
    if kode_status_pengiriman not in map_status_pengiriman:
        raise Exception("Error. Tolong masukkan bilangan bulat dari 1-5.")
    return map_status_pengiriman[kode_status_pengiriman]


@infinite_looper
def input_biaya():
    ## Digunakan untuk update, bukan untuk create
    biaya = float(input("Masukkan biaya pengiriman baru: "))
    if biaya < 0:
        raise Exception("Error. Biaya pengiriman tidak bisa negatif.")
    return berat_barang

@infinite_looper
def input_delivery_date():
    ## Digunakan untuk update, bukan untuk create
    tanggal = datetime.datetime.strptime(input("Masukkan tanggal pengiriman (format: tahun-bulan-tanggal): "), date_format).date()
    return tanggal

## Dictionary di bawah ini menghubungkan nama feature ke tiap fungsi input feature tersebut.
map_kolom_input = {'id': input_id_pengiriman,
                  'delivery_date': input_delivery_date,
                   'sender': input_nama_pengirim,
                   'sender_no': input_no_pengirim,
                   'address': input_alamat_tujuan,
                   'city': input_kota,
                   'recipient': input_nama_penerima,
                   'recipient_no': input_no_penerima,
                   'weight': input_berat_barang,
                   'type': input_jenis_barang,
                   'cost': input_biaya,
                   'status': input_status_pengiriman}

## List di bawah ini adalah features yang harus dimasukkan operator dari data pengirim saat pembuatan data pengiriman.
kolom_input_saat_pembuatan_data = ['sender', 'sender_no', 'address', 'city', 'recipient', 'recipient_no', 'weight', 'type']

def find_duplicate_data(input_data, data_pengiriman):
    ## Print seluruh data possible duplikat dan return True (jika ditemukan)
    ## Return False otherwise
    temp_dict = {key: [] for key in data_pengiriman}
    
    row_in_data = [input_data[key][0] for key in kolom_input_saat_pembuatan_data]

    for i in range(len(data_pengiriman['id'])):
        row_in_table = [data_pengiriman[key][i] for key in kolom_input_saat_pembuatan_data]
        if row_in_data == row_in_table:
            for key in temp_dict:
                temp_dict[key].append(data_pengiriman[key][i])

    if len(temp_dict['id']) != 0:
        print("\ntype code:\n1: Document | 2: Food | 3: Clothing | 4: Electronics | 5: Fragile | 6: Others")
        print(tabulate.tabulate(temp_dict, headers='keys', tablefmt ='grid', maxcolwidths=panjang_maks_kolom,stralign='left',numalign='left', colalign=['left' for x in temp_dict]))
        return True
    else:
        return False
    
@infinite_looper
def input_yes_or_no():
    is_yes = input("Y: Ya | N: Tidak\n")
    if is_yes.upper() == 'Y':
        return True
    elif is_yes.upper() == 'N':
        return False
    else:
        raise Exception("Input Invalid. Tolong masukkan Y atau N.")
    
@infinite_looper
def input_kolom():
    ## Untuk mengubah data, filtering, dan sorting
    kolom = input("Masukkan nama kolom (ketik BATAL untuk kembali ke menu sebelumnya): ")
    if kolom.upper() == 'BATAL':
        return
    elif kolom.lower() not in data_pengiriman:
        raise Exception("Error. Kolom tidak ditemukkan.")
    else:
        return kolom.lower()
    
def filtering_func(value, data_pengiriman, kolom):
    ## Untuk filtering
    ## Bukan decorator.
    def inner_filtering_func(indeks):
        if type(value) == str:
            return value.lower() in data_pengiriman[kolom][indeks].lower()
        else:
            return value == data_pengiriman[kolom][indeks]
    return inner_filtering_func

def get_filtered_indeks(value, data_pengiriman, kolom):
    return list(filter(filtering_func(value, data_pengiriman, kolom), range(len(data_pengiriman['id']))))

def sorting_func(data_pengiriman, kolom):
    ## Untuk membandingkan nilai-nilai pada kolom sedemikian rupa hingga indeksnya bisa diurutkan berdasarkan nilai-nilai tersebut.
    ## Bukan decorator.
    def inner_sorting_func(indeks):
        return data_pengiriman[kolom][indeks]
    return inner_sorting_func

def get_sorted_indeks(data_pengiriman, kolom, is_descending=False):
    ## Tidak dikonversi menjadi list karena output-nya sudah berupa list
    return sorted(range(len(data_pengiriman['id'])), key=sorting_func(data_pengiriman, kolom), reverse=is_descending)
    
def display_n_data(data_pengiriman, list_indeks):    
    temp_dict = {key:[data_pengiriman[key][indeks] for indeks in list_indeks] for key in data_pengiriman}
    print("\ntype code:\n1: Document | 2: Food | 3: Clothing | 4: Electronics | 5: Fragile | 6: Others")
    if len(list_indeks) == 0:
        ## Kalau tidak dipisah seperti ini, error karena maxcolwidths, strlalign, numalign, etc. perlu akses elemen (yang ada) tiap list di kolom
        ## Sedangkan list tiap kolom kosong
        print(tabulate.tabulate(temp_dict, headers='keys', tablefmt ='grid'))
    else:
        print(tabulate.tabulate(temp_dict, headers='keys', tablefmt ='grid', maxcolwidths=panjang_maks_kolom,stralign='left',numalign='left', colalign=['left' for x in temp_dict]))

def display_all_data(data_pengiriman):
    ## Lebih cepat dari yang di atas untuk printing seluruh data karena tidak perlu pemasukkan kembali ke temp_dict
    print("\ntype code:\n1: Document | 2: Food | 3: Clothing | 4: Electronics | 5: Fragile | 6: Others")
    print(tabulate.tabulate(data_pengiriman, headers='keys', tablefmt ='grid', maxcolwidths=panjang_maks_kolom,stralign='left',numalign='left', colalign=['left' for x in data_pengiriman]))



@infinite_looper
def display_data(data_pengiriman):
    to_print = """
    Pilihan menu:
    1. Tampilkan satu data pengiriman berdasarkan id
    2. Tampilkan seluruh data pengiriman
    3. Cari dan tampilkan data pengiriman
    4. Urut dan tampilkan data pengiriman
    5. Keluar
    """
    print(to_print)
    kode_input = int(input("Masukkan kode input: "))
    match kode_input:
        case 1:
            if len(data_pengiriman['id']) == 0:
                raise Exception("Data masih kosong.")

            id_data = input_id_pengiriman()
            indeks = find_index(data_pengiriman['id'], id_data)
    
            if indeks == -1:
                raise Exception(f"Data dengan id pengiriman {id_data} tidak ditemukan.")
            display_n_data(data_pengiriman, [indeks])

            return continue_token
        
        case 2:
            if len(data_pengiriman['id']) == 0:
                raise Exception("Data masih kosong.")
            display_all_data(data_pengiriman)
            return continue_token
        case 3:
            searchable_columns = ["sender", "recipient", "address", "city", "type", "status"]
            print(f"Kolom yang bisa dicari: | {' | '.join(searchable_columns)} |")
            kolom = input_kolom()
            if kolom == None: # input_kolom() -> 'BATAL'
                return continue_token
            elif kolom not in searchable_columns:
                raise Exception(f"Error. Tidak bisa melakukan pencarian pada kolom {kolom}")
            else:
                if kolom == "type" or kolom == "status":
                    kunci_pencarian = map_kolom_input[kolom]()
                else:
                    kunci_pencarian = input("Masukkan kata kunci pencarian: ")
                filtered_indeks = get_filtered_indeks(kunci_pencarian, data_pengiriman, kolom)
                display_n_data(data_pengiriman, filtered_indeks)
                return continue_token
        case 4:
            sortable_columns = ['id', 'delivery_date', 'weight', 'cost']
            print(f"Kolom yang bisa digunakan untuk pengurutan: | {' | '.join(sortable_columns)} |")
            kolom = input_kolom()
            if kolom == None: # Input = 'BATAL'
                return continue_token
            elif kolom not in sortable_columns:
                raise Exception(f"Error. Tidak bisa melakukan pengurutan berdasarkan kolom {kolom}")
            else:
                print("Urutkan dari yang terbesar?")
                is_descending = True if input("Y: Ya | Tekan apapun: Tidak\n").upper()  == 'Y' else False
                sorted_indeks = get_sorted_indeks(data_pengiriman, kolom, is_descending=is_descending)
                display_n_data(data_pengiriman, sorted_indeks)
                return continue_token

        case 5:
            return
        case _:
            raise Exception("Invalid input. Tolong ulangi input.")
            

@infinite_looper
def buat_data_pengiriman(data_pengiriman):
    to_print = """
    Pilihan menu:
    1. Buat data pengiriman
    2. Keluar
    """
    print(to_print)
    kode_input = int(input("Masukkan kode input: "))
    match kode_input:
        case 1:
            print("-----Note: PenguinExpress hanya melayani pengiriman dalam pulau Jawa-----")
            print("Apa pengirim menyetujui hal ini?")
            is_yes = input_yes_or_no()
            if not is_yes:
                return continue_token
            print("Apa anda ingin memasukkan custom id pengiriman (primary key)?\nJika tidak, maka anda dapat langsung memasukkan data pengiriman (penambahan id pengiriman akan ditangani sistem).")
            is_custom_id_pengiriman = True if input("Y: Ya | Tekan apapun: Tidak\n").upper()  == 'Y' else False
            
            if is_custom_id_pengiriman:
                id_data = input_id_pengiriman()
                if id_data in data_pengiriman['id']:
                    raise Exception(f"Error. Data dengan id pengiriman {id_data} sudah ada.")
            else:
                id_data = None


            ## Input data yang akan dibuat.
            ## Kenapa formatnya dictionary of list meskipun element list-nya hanya satu?
            ## Untuk memudahkan print baris data yang akan ditambahkan dengan tabulate.
            ## map_kolom_input adalah dictionary dimana tiap key-nya adalah feature yang ada pada data_pengiriman, valuenya adalah fungsi untuk meng-input features tersebut.
            input_data = {key: [map_kolom_input[key]()] for key in kolom_input_saat_pembuatan_data}
            
            ## In case 
            if find_duplicate_data(input_data, data_pengiriman):
                print("Hmmm. Data yang dimasukkan sepertinya mirip dengan data yang ada sebelumnya. Lanjutkan pembuatan data?")
                is_yes = input_yes_or_no()
                if not is_yes:
                    return continue_token
        
            jarak = hitung_jarak(koordinat_kota[kota_pengiriman], koordinat_kota[input_data['city'][0]])
            input_data['cost'] = [tarif_pengiriman(jarak, input_data['weight'][0], price_per_distance, base_price)]
        
            print(tabulate.tabulate(input_data, headers='keys', tablefmt ='grid', maxcolwidths=panjang_maks_kolom_konfirmasi_penambahan_data,stralign='left',numalign='left', colalign=['left' for x in input_data]))
            print("Rincian data pengiriman yang akan dibuat adalah seperti di atas. Apakah pengirim menyetujui biaya pengiriman?")
            is_yes = input_yes_or_no()
            if not is_yes:
                    return continue_token
        
            if id_data == None:
                input_data['id'] = [max(data_pengiriman['id']) + 1] ## Kalau tidak memilih memasukkan id pengiriman, maka id pengiriman data baru adalah id tertinggi plus satu. 
            else:
                input_data['id'] = [id_data]
                
            input_data['delivery_date'] = [datetime.datetime.now().date()] 
            input_data['status'] = ['ON-PROCESS']
            for key in input_data:
                data_pengiriman[key].append(input_data[key][0])
        
            print("Data berhasil dibuat. Rincian detail data yang telah dibuat adalah sebagai berikut:")
            display_n_data(data_pengiriman, [-1])
            input_data.clear()
            return continue_token
            
        case 2:
            print("Apa anda yakin ingin keluar dari menu pembuatan data?")
            agreement = input("Y: Ya | Tekan apapun: Kembali\n")
            if agreement.upper() == 'Y':
                return
            else:
                return continue_token
        case _:
            raise Exception("Invalid input. Tolong ulangi input.")

@infinite_looper
def update_data_pengiriman(data_pengiriman):
    to_print = """
    Pilihan menu:
    1. Ubah data pengiriman
    2. Keluar
    """
    print(to_print)
    kode_input = int(input("Masukkan kode input: "))
    match kode_input:
        case 1:
            id_data = input_id_pengiriman()
            indeks = find_index(data_pengiriman['id'], id_data)
    
            if indeks == -1:
                raise Exception(f"Data dengan id pengiriman {id_data} tidak ditemukan.")
                
            display_n_data(data_pengiriman, [indeks])
            print("Apa anda ingin mengubah data ini?")
            is_yes = input_yes_or_no()
            if not is_yes:
                    return continue_token
                
            kolom = input_kolom()
            if kolom == None: # input_kolom() ->  'BATAL'
                return continue_token
            elif kolom == 'id':
                raise Exception("Error. Tidak bisa mengubah id pengiriman (primary key).")    
            elif kolom == 'city' or kolom == 'address':
                ## Jika ingin mengganti alamat atau kota tujuan, maka pengirim dikenakan tarif tambahan, yaitu biaya dari kota tujuan sebelumnya ke kota tujuan yang baru.
                alamat_tujuan_lama = data_pengiriman['address'][indeks]
                kota_tujuan_lama = data_pengiriman['city'][indeks]
                alamat_tujuan_baru = map_kolom_input['address']()
                kota_tujuan_baru = map_kolom_input['city']()

                jarak_tambahan = hitung_jarak(koordinat_kota[kota_tujuan_lama], koordinat_kota[kota_tujuan_baru])
                biaya_tambahan = tarif_pengiriman(jarak_tambahan, data_pengiriman['weight'][indeks], price_per_distance, base_price)
                print(f"alamat : {alamat_tujuan_lama} --> {alamat_tujuan_baru}")
                print(f"kota: {kota_tujuan_lama} --> {kota_tujuan_baru}")
                print(f"Biaya tambahan yang harus dibayar adalah {biaya_tambahan}. Apakah pengirim menyetujui hal ini?")
                is_yes = input_yes_or_no()
                
                if not is_yes:
                    return continue_token

                data_pengiriman['address'][indeks] = alamat_tujuan_baru
                data_pengiriman['city'][indeks] = kota_tujuan_baru
                data_pengiriman['cost'][indeks] += biaya_tambahan

                print("Data berhasil diubah. Data pengiriman yang baru adalah sebagai berikut.")
                display_n_data(data_pengiriman, [indeks])
                return continue_token

            else:
                old_value = data_pengiriman[kolom][indeks]
                new_value = map_kolom_input[kolom]()
                print(f"Nilai lama {kolom} pengiriman PE{id_data} adalah: {old_value}.\nNilai baru {kolom} pengiriman PE{id_data} adalah: {new_value}.\nUbah data pengiriman?")
                is_yes = input_yes_or_no()
                
                if not is_yes:
                    return continue_token
                    
                data_pengiriman[kolom][indeks] = new_value

                print("Data berhasil diubah. Data pengiriman yang baru adalah sebagai berikut.")
                display_n_data(data_pengiriman, [indeks])
                return continue_token
                            
        case 2:
            print("Apa anda yakin ingin keluar dari menu pengubahan data?")
            agreement = input("Y: Ya | Tekan apapun: Kembali\n")
            if agreement.upper() == 'Y':
                return
            else:
                return continue_token
        case _:
            raise Exception("Invalid input. Tolong ulangi input.")
        


@infinite_looper
def hapus_data_pengiriman(data_pengiriman):
    to_print = """
    Pilihan menu:
    1. Hapus data pengiriman
    2. Keluar
    """
    print(to_print)
    kode_input = int(input("Masukkan kode input: "))
    match kode_input:
        case 1:
            id_data = input_id_pengiriman()
            indeks = find_index(data_pengiriman['id'], id_data)
    
            if indeks == -1:
                raise Exception(f"Data dengan id pengiriman {id_data} tidak ditemukan.")
                
            display_n_data(data_pengiriman, [indeks])
            print("Apa anda ingin menghapus data ini?")
            is_yes = input_yes_or_no()
            if not is_yes:
                    return continue_token

            for key in data_pengiriman:
                data_pengiriman[key].pop(indeks)

        
            print("Data berhasil dihapus.")
            return continue_token
               
        case 2:
            print("Apa anda yakin ingin keluar dari menu penghapusan data?")
            agreement = input("Y: Ya | Tekan apapun: Kembali\n")
            if agreement.upper() == 'Y':
                return
            else:
                return continue_token
        case _:
            raise Exception("Invalid input. Tolong ulangi input.")
        

@infinite_looper
def buat_kata_sandi():
    kata_sandi_1 = input_nonempty_string("Masukkan kata sandi baru: ")
    kata_sandi_2 = input_nonempty_string("Ulangi masukkan kata sandi baru: ")
    if kata_sandi_1 != kata_sandi_2:
        raise Exception("Error. Kata sandi yang dimasukkan tidak sesuai.")
    return kata_sandi_2

@infinite_looper
def pengaturan():
    global kata_sandi ## Diperlukan untuk mengganti kata sandi di opsi 1.
    opsi_1 = "Buat kata sandi" if kata_sandi == None else "Ubah kata sandi"
    to_print = f"""
    Pilihan menu

    1. {opsi_1}
    2. Keluar
    """
    print(to_print)
    kode_input = int(input("Masukkan kode input: "))
    match kode_input:
        case 1:
            print("Apa anda yakin ingin membuat kata sandi baru?")
            is_yes = input_yes_or_no()
            if not is_yes:
                return continue_token

            if kata_sandi != None:
                kata_sandi_lama = input("Masukkan kata sandi lama: ")
                if kata_sandi_lama != kata_sandi:
                    raise Exception("Kata sandi salah.")
            
            kata_sandi = buat_kata_sandi()
            print("Kata sandi baru berhasil dibuat.")
            
            return continue_token
        
        case 2:
            print("Apa anda yakin ingin keluar dari pengaturan?")
            agreement = input("Y: Ya | Tekan apapun: Kembali\n")
            if agreement.upper() == 'Y':
                return
            else:
                return continue_token

        case _:
            raise Exception("Invalid input. Tolong ulangi input.")



@infinite_looper
def menu_utama():
    to_print = f"""
    PenguinExpress Kantor {kota_pengiriman}.

    Pilihan menu:
    1. Tampilkan Data Pengiriman
    2. Buat Data Pengiriman
    3. Hapus Data Pengiriman
    4. Edit Data Pengiriman
    5. Pengaturan
    6. Keluar
    """
    print(to_print)
    kode_input = int(input("Masukkan kode input: "))
    match kode_input:
        case 1:
            display_data(data_pengiriman)
            return continue_token
        case 2:
            buat_data_pengiriman(data_pengiriman)
            return continue_token
        case 3:
            hapus_data_pengiriman(data_pengiriman)
            return continue_token
        case 4:
            update_data_pengiriman(data_pengiriman)
            return continue_token
        case 5:
            pengaturan()
            return continue_token
        case 6:
            print("Apa anda yakin ingin keluar dari menu utama?")
            agreement = input("Y: Ya | Tekan apapun: Kembali\n")
            if agreement.upper() == 'Y':
                return
            else:
                return continue_token
        case _:
            raise Exception("Invalid input. Tolong ulangi input.")


@infinite_looper
def entry_menu():
    to_print = """
    Selamat datang di PenguinExpress!

    Pilihan menu:
    1. Masuk menu utama
    2. Keluar
    """
    print(to_print)
    kode_input = int(input("Masukkan kode input: "))
    match kode_input:
        case 1:
            if kata_sandi == None:
                print("\nAnda belum membuat kata sandi. Melanjutkan ke menu utama...")
            else:
                kata_sandi_input = input("Masukkan kata sandi: ")
                if kata_sandi_input != kata_sandi:
                    raise Exception("Kata sandi salah.")
                else:
                    print("Melanjutkan ke menu utama...")

            menu_utama()
            return continue_token
        case 2:
            print("Apa anda yakin ingin keluar dari program?")
            agreement = input("Y: Ya | Tekan apapun: Kembali\n")
            if agreement.upper() == 'Y':
                return
            else:
                return continue_token
        case _:
            raise Exception("Invalid input. Tolong ulangi input.")



entry_menu()


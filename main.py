catatan = []

def tambah_catatan():
    mapel = input("Masukkan mata pelajaran: ")
    topik = input("Masukkan topik: ")
    durasi = int(input("Masukkan durasi belajar (menit): "))
    
    # Menyimpan data dalam bentuk dictionary (mudah dipahami pemula)
    catatan_baru = {
        "mapel": mapel,
        "topik": topik,
        "durasi": durasi
    }
    
    catatan.append(catatan_baru)
    print(f"✓ Catatan ditambahkan: {mapel} - {topik} ({durasi} menit)\n")

def lihat_catatan():
    if len(catatan) == 0:
        print("\n📝 Belum ada catatan belajar. Mulai tambahkan catatan!\n")
    else:
        print("\n=== Daftar Catatan Belajar ===")
        for i, data in enumerate(catatan, 1):
            print(f"{i}. {data['mapel']} - {data['topik']}")
            print(f"   Durasi: {data['durasi']} menit")
        print()

def total_waktu():
    if len(catatan) == 0:
        print("\n📝 Belum ada catatan belajar. Mulai tambahkan catatan!\n")
    else:
        total = sum(data["durasi"] for data in catatan)
        jam = total // 60
        menit = total % 60
        
        print(f"\n⏱️  Total Waktu Belajar: {total} menit")
        print(f"   ({jam} jam {menit} menit)\n")

def ringkasan_mingguan():
    if len(catatan) == 0:
        print("\n📝 Belum ada catatan belajar.\n")
        return
    
    print("\n=== Ringkasan Mingguan ===")
    
    # Kelompokkan by mapel
    mapel_dict = {}
    for data in catatan:
        mapel = data["mapel"]
        if mapel not in mapel_dict:
            mapel_dict[mapel] = 0
        mapel_dict[mapel] += data["durasi"]
    
    total_semua = sum(mapel_dict.values())
    
    # Tampilkan ringkasan
    for mapel, durasi in sorted(mapel_dict.items(), key=lambda x: x[1], reverse=True):
        jam = durasi // 60
        menit = durasi % 60
        persentase = (durasi / total_semua * 100) if total_semua > 0 else 0
        print(f"{mapel}: {durasi} menit ({jam}j {menit}m) - {persentase:.1f}%")
    
    total_jam = total_semua // 60
    total_menit = total_semua % 60
    print(f"\nTotal: {total_semua} menit ({total_jam}j {total_menit}m)\n")

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Ringkasan mingguan")
    print("5. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        ringkasan_mingguan()
    elif pilihan == "5":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")
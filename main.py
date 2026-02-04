catatan = []

def tambah_catatan():
    print("\n📚 ✨ Yuk, catat belajar kamu! ✨")
    mapel = input("  📖 Mata pelajaran: ")
    topik = input("  📝 Topik: ")
    durasi = int(input("  ⏱️  Durasi belajar (menit): "))
    
    # Menyimpan data dalam bentuk dictionary (mudah dipahami pemula)
    catatan_baru = {
        "mapel": mapel,
        "topik": topik,
        "durasi": durasi
    }
    
    catatan.append(catatan_baru)
    print(f"\n🎉 Yeay! Catatan ditambahkan!")
    print(f"   📚 {mapel} | 📝 {topik} | ⏱️  {durasi} menit")
    print(f"   Semangat terus! 💪\n")

def lihat_catatan():
    if len(catatan) == 0:
        print("\n� Opps! Belum ada catatan belajar nih...")
        print("   Yuk, mulai tambahkan catatan! 📚\n")
    else:
        print("\n" + "="*45)
        print("         📚 Daftar Catatan Belajar 📚")
        print("="*45)
        for i, data in enumerate(catatan, 1):
            print(f"\n  {i}. 📖 {data['mapel'].upper()}")
            print(f"     └─ 📝 {data['topik']}")
            print(f"     └─ ⏱️  {data['durasi']} menit")
        print("\n" + "="*45 + "\n")

def total_waktu():
    if len(catatan) == 0:
        print("\n� Belum ada catatan belajar nih!")
        print("   Yuk, mulai catat sesi belajar kamu! 📚\n")
    else:
        total = sum(data["durasi"] for data in catatan)
        jam = total // 60
        menit = total % 60
        
        print("\n" + "="*45)
        print("       ⏱️  TOTAL WAKTU BELAJAR ⏱️")
        print("="*45)
        print(f"\n  📊 Total: {total} menit")
        print(f"  🕐 Setara: {jam} jam {menit} menit")
        print(f"\n  Hebat! Terus semangat! 💪✨")
        print("\n" + "="*45 + "\n")

def ringkasan_mingguan():
    if len(catatan) == 0:
        print("\n� Belum ada catatan belajar.")
        print("   Yuk, mulai catat! 📚\n")
        return
    
    print("\n" + "="*50)
    print("       📈 RINGKASAN MINGGUAN BELAJAR 📈")
    print("="*50)
    
    # Kelompokkan by mapel
    mapel_dict = {}
    for data in catatan:
        mapel = data["mapel"]
        if mapel not in mapel_dict:
            mapel_dict[mapel] = 0
        mapel_dict[mapel] += data["durasi"]
    
    total_semua = sum(mapel_dict.values())
    
    # Tampilkan ringkasan
    print()
    for idx, (mapel, durasi) in enumerate(sorted(mapel_dict.items(), key=lambda x: x[1], reverse=True), 1):
        jam = durasi // 60
        menit = durasi % 60
        persentase = (durasi / total_semua * 100) if total_semua > 0 else 0
        bar_length = int(persentase / 5)
        bar = "█" * bar_length + "░" * (20 - bar_length)
        print(f"  {idx}. 📚 {mapel.upper()}")
        print(f"     [{bar}] {persentase:.1f}%")
        print(f"     ⏱️  {durasi} menit ({jam}j {menit}m)\n")
    
    total_jam = total_semua // 60
    total_menit = total_semua % 60
    print("="*50)
    print(f"  📊 Total Keseluruhan: {total_semua} menit")
    print(f"  🕐 Setara: {total_jam} jam {total_menit} menit")
    print(f"  🌟 Kamu hebat! Terus semangat! 💪")
    print("="*50 + "\n")

def menu():
    print("\n" + "="*50)
    print("        📚 STUDY LOG APP - SEMANGAT BELAJAR! 📚")
    print("="*50)
    print("\n  1️⃣  Tambah catatan belajar")
    print("  2️⃣  Lihat catatan belajar")
    print("  3️⃣  Total waktu belajar")
    print("  4️⃣  Ringkasan mingguan")
    print("  5️⃣  Keluar")
    print("\n" + "="*50)

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
        print("\n🎓 Sampai jumpa! Terus semangat belajar ya! 💪✨")
        print("\n     Jadilah versi terbaik dirimu! 🌟\n")
        break
    else:
        print("\n❌ Pilihan tidak valid. Coba lagi! 😊\n")
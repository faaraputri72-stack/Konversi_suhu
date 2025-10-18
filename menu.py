# No 5
print("--> Menu Warung <--")
menu = {
    "Rica Rica embrio": 19000,
    "Ayam betutu California": 14000,
    "Es stecu": 3000,
    "Kopi luwak hytam": 8000
}

for m, h in menu.items():
    print(m, ":", h)

total = 0
while True:
    pilih = input("\nPilih menu (ketik 'selesai' untuk berhenti): ")
    if pilih.lower() == "selesai":
        break
    if pilih in menu:
        jumlah = int(input("Jumlah pesanan: "))
        total += menu[pilih] * jumlah
    else:
        print("Menu tidak ada, coba lagi.")

if total > 100000:
    potongan = total * 0.1
    total -= potongan
    print("diskon 10%")

print("Total bayar: Rp", int(total))
print("Tengss ya, jan lupa balik")

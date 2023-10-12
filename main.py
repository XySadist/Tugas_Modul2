# Data expenses
expenses = [
   {'tanggal': '2023-07-25', 'deskripsi': 'Makan Siang', 'jumlah': 50000},
   {'tanggal': '2023-07-25', 'deskripsi': 'Transportasi', 'jumlah': 25000},
   {'tanggal': '2023-07-26', 'deskripsi': 'Belanja', 'jumlah': 100000},
]

# Fungsi 1: add_expense
def add_expense(expenses, tanggal, deskripsi, jumlah):
    new_expense = {'tanggal': tanggal, 'deskripsi': deskripsi, 'jumlah': jumlah}
    return expenses + [new_expense]

# Fungsi 2: calculate_total_expenses
calculate_total_expenses = lambda expenses: sum(expense['jumlah'] for expense in expenses)

# Fungsi 3: get_expenses_by_date
def get_expenses_by_date(expenses, tanggal):
    return [expense for expense in expenses if expense['tanggal'] == tanggal]

# Fungsi 4: generate_expenses_report
generate_expenses_report = lambda expenses: (f"{expense['tanggal']} - {expense['deskripsi']} - Rp {expense['jumlah']}" for expense in expenses)

# Fungsi 5: Modifikasi fungsi add_expense_interactively
def add_expense_interactively(expenses):
    date = input("Masukkan tanggal pengeluaran (YYYY-MM-DD): ")
    description = input("Masukkan deskripsi pengeluaran: ")
    amount = int(input("Masukkan jumlah pengeluaran: "))
    new_expenses = add_expense(expenses, date, description, amount)
    print("Pengeluaran berhasil ditambahkan.")
    return new_expenses

# Fungsi 6: Modifikasi fungsi get_user_input
get_user_input = lambda command: int(input(command))

# Fungsi 7: Modifikasi fungsi view_expenses_by_date
def view_expenses_by_date(expenses):
    date = input("Masukkan tanggal (YYYY-MM-DD): ")
    expenses_on_date = get_expenses_by_date(expenses, date)
    print(f"\nPengeluaran pada tanggal {date}:")
    for expense in expenses_on_date:
        print(f"{expense['deskripsi']} - Rp {expense['jumlah']}")

# Fungsi 8: Modifikasi fungsi view_expenses_report
def view_expenses_report(expenses):
    print("\nLaporan Pengeluaran Harian:")
    for entry in generate_expenses_report(expenses):
        print(entry)

# Fungsi 9: Fungsi display_menu
def display_menu():
   print("\n===== Aplikasi Pencatat Pengeluaran Harian =====")
   print("1. Tambah Pengeluaran")
   print("2. Total Pengeluaran Harian")
   print("3. Lihat Pengeluaran berdasarkan Tanggal")
   print("4. Lihat Laporan Pengeluaran Harian")
   print("5. Keluar")

# Fungsi 10: Modifikasi fungsi main
def main():
    global expenses
    while True:
        display_menu()
        choice = get_user_input("Pilih menu (1/2/3/4/5): ")
        if choice == 1:
            expenses = add_expense_interactively(expenses)
        elif choice == 2:
            total_expenses = calculate_total_expenses(expenses)
            print(f"\nTotal Pengeluaran Harian: Rp {total_expenses}")
        elif choice == 3:
            view_expenses_by_date(expenses)
        elif choice == 4:
            view_expenses_report(expenses)
        elif choice == 5:
            print("Terima kasih telah menggunakan aplikasi kami.")
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih menu yang benar.")

if __name__ == "__main__":
    main()

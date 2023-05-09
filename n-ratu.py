nomor_solusi = 0

def solve_n_queens(n):
    print(f"=== Jumlah ratu sebanyak {n} pada papan catur {n}x{n} ===")
    print()

    # inisialisasi papan catur n x n
    board = [[0] * n for _ in range(n)]
    
    def is_valid(row, col):
        # periksa apakah tidak ada ratu pada kolom yang sama
        for i in range(row):
            if board[i][col] == 1:
                return False
        
        # periksa diagonal kiri atas ke kanan bawah
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        # periksa diagonal kanan atas ke kiri bawah
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 1:
                return False
        
        return True
    
    def backtrack(row):
        global nomor_solusi
        if row == n:
            # semua ratu telah ditempatkan pada papan catur
            # cetak solusinya
            nomor_solusi += 1
            print(f"Solusi #{nomor_solusi}")
            for i in range(n):
                for j in range(n):
                    print(board[i][j], end=" ")
                print()
            print()
            
        for col in range(n):
            if is_valid(row, col):
                # tempatkan ratu pada papan catur
                board[row][col] = 1
                
                # lanjutkan ke baris selanjutnya
                backtrack(row+1)
                
                # kembali ke keadaan sebelumnya dan coba kolom berikutnya
                board[row][col] = 0
                
    # mulai dari baris pertama
    backtrack(0)

    global nomor_solusi
    if nomor_solusi == 0:
        print("--- Solusi tidak ditemukan ---\n")
    # reset jumlah solusi
    nomor_solusi = 0

# contoh pemanggilan fungsi
solve_n_queens(3) # untuk 3 ratu pada papan 3x3
solve_n_queens(4) # untuk 4 ratu
solve_n_queens(5) # untuk 5 ratu
# solve_n_queens(6) # untuk 6 ratu
# solve_n_queens(7) # untuk 7 ratu
# solve_n_queens(8) # untuk 8 ratu

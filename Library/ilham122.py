def penjumlahan(A, B):   
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Error: Ordo matriks harus sama.")
        return None
    hasil = [] 
    for i in range(len(A)):
        baris = []       
        for j in range(len(A[0])):
            baris.append(A[i][j] + B[i][j])
        hasil.append(baris)
    return hasil


def pengurangan(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Error: Ordo matriks harus sama.")
        return None
    hasil = []
    for i in range(len(A)):
        baris = []
        for j in range(len(A[0])):
            baris.append(A[i][j] - B[i][j])
        hasil.append(baris)
    return hasil


def perkalian(A, B):
    if len(A[0]) != len(B):
        print("Error: Jumlah kolom matriks pertama harus sama dengan jumlah baris matriks kedua.")
        return None
    hasil = []
    for i in range(len(A)):
        baris = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(B)):
                total += A[i][k] * B[k][j]
            baris.append(total)
        hasil.append(baris)
    return hasil

t = int(input())
simpan_nilai = []
w = 0
while w < t:
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    q = int(input())
        
    jumlah_array = sum(array[:k])
    nilai_min = jumlah_array
    nilai_max = jumlah_array
        
    for h in range(1, k+1):
        jumlah_array = sum(array[:h])
        nilai_min = min(nilai_min, jumlah_array)
        nilai_max = max(nilai_max, jumlah_array)
        for i in range(1, n - h + 1):
            jumlah_array = jumlah_array - array[i - 1] + array[i + h - 1]
            nilai_min = min(nilai_min, jumlah_array)
            nilai_max = max(nilai_max, jumlah_array)

    if q == 1:
        simpan_nilai.append(nilai_max)
    if q == 2:
        simpan_nilai.append(nilai_min)
    w += 1

for nilai in simpan_nilai:
    print(nilai)
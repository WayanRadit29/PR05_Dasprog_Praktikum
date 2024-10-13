N = int(input())
bil_zamtum = list(map(int,input().split()))
kali = 1

for i in range(N):
    for j in range(i+1, N):
        if bil_zamtum[i] != bil_zamtum[j]:
            kali *= bil_zamtum[i] ^ bil_zamtum[j]
        else:
            kali = 0
            break

print(kali)


    


            

              
              
               


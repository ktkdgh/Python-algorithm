n = int(input())
cnt = 99

if n < 100:
    cnt = n
else:
    for i in range(111, n+1):
        d = i//100 - (i%100 // 10)
        if d == (i%100//10) -i%10:
            cnt+= 1
print(cnt)
        

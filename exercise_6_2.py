n=100
total=0
while n<10000:
    if n%5==0:
        total=total+n
        n=n+1
    else:
        n=n+1
        continue

else:
    print(total)

for x in range(100,10000,5):
    total=total+x
else:
    print(total)

    


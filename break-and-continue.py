count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
    
#odd numbers only
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)
    
#"ELSE" for looping
count = 0
while(count<5):
    print(count)
    count += 1
else:
    print("count value reached %d" %(count))
    
for i in range(1, 10):
    if (i % 5 == 0):
        break
    print(i)
else:
    print("lol")
COUNT = 0
ip = int(input("Enter Number of Terms: "))
a, b = 0, 1

if ip <= 0:
    print("Invalid Input")
    quit()

for i in range(ip):
    if i == 0 or i == 1:
        print(i)
        COUNT += 1
    else:
        nth = a + b
        a = b
        b = nth
        print(nth)
        COUNT += 4

print("Steps required using Counter:", COUNT)

     
#a   b  nth
#0   1   1
#1   1   2
#1   2   3
#2   3   5
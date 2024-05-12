a = 3
if (a != 3):
    print(a)
else:
    print("value")
    print("value does not match")

    obj = [1,2,3,4,5,"ranju"]
    for i in obj:
        print(i*2)

        #sum of 1st 5 numbs
    sum= 0
    for i in range(1,6):
        sum += i
    print(sum)

    for k in range(1, 10, 3):
        print(k)

    a = 4
    while a > 2:
        print("while",a)
        if(a == 1):
         a-= 1

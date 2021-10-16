import matplotlib.pyplot as plt


a = int(input("Enter a: "))
b = int(input("Enter b: "))

for x in range(1, 101):
    storeList = []
    stoppingTime = []
    repeatList = []
    values = []
    i = 0
    while True:
        
        flag = len(set(storeList)) == len(storeList)
        if flag == 1:
            repeatList.append(x)
        elif flag == 0:
            break
        
        print(x, end=", ")
        storeList.append(x)

        i += 1
        stoppingTime.append(i)

        if x % 2 == 0:
            x = int(x / 2)
        else:
            x = a*x + b 

    #values.append(min(storeList))
    #print(values)
    plt.xlim(0, 100)
    plt.ylim(0, 1000)
            
    storeList.sort()
    plt.plot(stoppingTime, storeList)
    
    plt.yscale("linear")
    plt.title("Plot of Hailstone Numbers vs their initial Values")
    print("\n")


plt.show()

'''
Steps: Given a number x, if x is even, do x/2; if x is odd, perform ax + b; now put x = ax + b and continue until a repeating pattern starts occuring. As soon as a number in the list
repeats, terminate. 

'''

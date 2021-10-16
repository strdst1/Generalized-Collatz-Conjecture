import matplotlib.pyplot as plt

#input values 
a = int(input("Enter a: "))
b = int(input("Enter b: "))

#to compute first n-1 sequences, here n = 101. 
for x in range(1, 101):
    storeList = []
    stoppingTime = []
    repeatList = []
    values = []
    i = 0
    
    #defining the algorithm.
    while True:
        
        #checking if the sequence comes out to be unique, terminates if not unique. 
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
    
    #setting limits and plotting. 
    plt.xlim(0, 100)
    plt.ylim(0, 1000)
            
    storeList.sort()
    plt.plot(stoppingTime, storeList)
    
    plt.yscale("linear")
    plt.title("Plot of Hailstone Numbers vs their initial Values")
    print("\n")


plt.show()



for i in range(0,7):
    j=0
    while(j<=i):
        if(j==0 or i==j):
            print("1",end="")
        else:
            binom=1
            binom=int(binom*(i-j+1)/j)
            print(binom, end="")
        j=j+1
    print()

#  Star pattern for 
    #          *
    #       *  *  *
    #    *  *  *  *  * 
n=int(input("Enter value of n :"))
for i in range(1,n+1):
    print(" "*(n-i) ,end="")
    print("*"*(2*i-1), end="")
    print("")
    

# Star pattern
     #   *
    #    **
    #    *** 

n=int(input("Enter value of n :"))
for i in range(1,n+1):
    print("*"*(i), end="")
    print("")


# ***
# * *
# ***
n=int(input("Enter value of n :"))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*(n), end="")
        print("")
    else:
        print("*"*(1), end="")
        print(" "*(n-2) ,end="")
        print("*"*(1), end="")
        print("")

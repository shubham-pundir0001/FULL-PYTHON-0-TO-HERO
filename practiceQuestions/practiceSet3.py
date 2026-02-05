# Program to check spam msg.
a1="click this"
b1='free'
c1='''buy now'''
temp=input("Enter a msg:") 
if((a1 in temp) or (b1 in temp) or (c1 in temp) ):
    print("Spam msg....!")
else:
    print("Safe msg..!")


# 2. Program to print table from a for loop 
n=int(input("Enter a number :"))
for i in range(1,11):
    print(f"{n}X{i}={n*i}")


# 3. Program to print reverse table from a for loop 
n=int(input("Enter a number :"))
for i in range(1,11):
    print(f"{n}X{11-i}={n*(11-i)}")
# 1.Program to take a username and print good afternoon and name:!
name=input("Enter your name:")
print("Hello good afternoon:"+name)

# 2.Program to detect double space in a string 
temp="My name is shubham  Pundir"
print(temp.find("  "))

# 3.Program to find the gratest of four numbers entered by user.
a=int(input("Enter first number:"))
b=int(input("Enter Second number:"))
c=int(input("Enter Third number:"))
d=int(input("Enter Fourth number:"))
if (a>b and a>c and a>d):
    print(f"First number is greatest:{a}")
elif (b>c and b>d):
    print(f"Second number is greatest:{b}")
elif (c>d):
    print(f"third number is greatest:{c}")
else:
    print(f"Fourth number is greatest:{d}")
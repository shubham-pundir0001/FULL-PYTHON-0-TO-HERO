# Data Types in Python
# 1.Numeric Data Types
# integer
n=10
print(n)
print(type(n))

# float
f=2.4
print(f)
print(type(f))

#complex
C1=complex(4,6)
print(C1)
print(type(C1))
print(C1.real) #real part in complex data type
print(C1.imag) #imaginary part in complex data type

# 2.Sequence Data type
#String
name="shubham Pundir"
print("name:"+name)
print(type(name))

# List
mylist=[2,1,6,3,5,9]
print(mylist)
print(type(mylist))
print(mylist[2])

# Tuple
mytup=(6,5,1,8,4,3,7)
print(mytup)
print(type(mytup))

# 3.Mapping Type
# Dictionary
mydict={
    "name":"shubham",
    "RollNo":63,
    "Age":20
}
print(mydict)
print(type(mydict))

# 4.Boolean
# bool
mybool=True
print(mybool)
print(type(mybool))

# 5.Set Type
# set
myset={2,4,1,5,9} # values should be unique no duplicacy , mutable,unordered, unindexed.
print(myset)
print(type(myset))

# frozen set 
myfrozenset=frozenset(["cat" , "dog", "birds"])
print(myfrozenset)
print(type(myfrozenset))
print("cat" in myfrozenset)

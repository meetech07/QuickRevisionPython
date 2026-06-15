# function

# def hlo():                                #function name 
#     print("Radha Radha")
#     print("Radha Radha")
#     print("Radha Radha")
#     print("Radha Radha")
#     print("Radha Radha")



# hlo()


# def add(a,b):   # paramitar 
#     print(a+b)


# add(10,20)   # argument  


# type of Arguments

# 1. positional Arguments : ab ye kya hota hai hm sabhi paramitar me argument set karte hai matalb value dalte hai ek
# ek bhi paramitar me value miss hua to fuction run nahi karega.
# 1. Positional — order matters

# Example

# def add(x,y):
#     return x+y

# print(add(5,6))


# default ARGUMENTS : MATALB SAMJHO agr hm kisi bhi paramitar me dairet valu ko hi dal de tab bhi use default Argment bolte hai 
# Default — works even without passing a value

# Example. 

# def greet(name = "manish"):
#     print(f"hlo {name}")

# greet();

# greet("bounty")    # ab kya hoga name me bounty chala jayega esi ko bolte hai default Argument.

# 3. keyword Argument : ka maalb samjho agr mera paramitar ka valu hm keward yani ki hm variabule name se bhi de sakte hai
# Keyword — pass in any order.

# Example.

def info(age,name):
    print(f"my name is {name} and my age is {age}")

info(name = "manish Singh", age=21)




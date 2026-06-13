from tokenize import String


print("manish Singh");

# Variables
# Think of a variable as a labelled box — you put a value inside and refer to it by the label whenever you need it.
name = "Manish"
age  = 21
city = "Sasaram"

# Rules — these will cause errors:

# ❌  1name = "x"  → can't start with a number
# ❌  my name = "x"  → no spaces allowed
# ❌  my-name = "x"  → no special characters (except underscore)


# Naming Conventions
# camelCase  → myVariableName
# PascalCase → MyVariableName
# snake_case → my_variable_name      this is a best nameing convention


age =21;
name = "manish Singh";
#variyabul name printing do dypes line no. 6,7
print(f"my name is {name} or mera age {age} etna hai ");
print("my name is",name,"may ages is a",age);

#data type
"""What are Data Types?
Every value in Python has a type that tells Python
 what kind of data it is and what you can do with it. You don't need to declare types — Python figures it out automatically.

"""
a = 21;
b = "manish";
c = 3.43;
d = True;

print(type(a));
print(type(b));
print(type(c));
print(type(d));

# Strings & Type Conversion
# Each character in a string is stored with its own Unicode number. That's why strings use more memory than integers.

print(ord("B"));   # → 66  (Unicode of B)
print(chr(64))   # → "@" (Character from Unicode)

# the "ord" function the use the print a Unicode number and the synex is 
# ord("pass the value")

# String Indexing

name = "ManishSingh";
print(name[4]);
print(name[-7]);

# 0   1   2   3   4   5   6   7   8   9   10      positive indexing namr[4] = s
# M   a   n   i   s   h   S   i   n   g   h
#-11 -10 -9  -8  -7  -6  -5  -4  -3   -2  -1      negetive indexing name[-7] = s

# String Slicing
# Slicing cuts out a piece of a string. Syntax: string[start : stop : step] — note that stop index is 

fist_name ="manish"
print(fist_name[0:6:1]);
print(fist_name[0:len(fist_name):1]);     # len ek lenght hai jise total index ka namuber nahi total no. of letar ya chatactor ko replsent karta hai 
# formula or len() function.   = total indexs + 1 
# ab iska matalb samjho fist_name[0:6:1]. 
#  1. ye jo fist_name hai o ek variabul hai jo name ko holde kiya hai memory me 
#  2.  fist_name[0:6:1]   yaha 0 ka matal start kaha se hoga Sting Slicing ke liye
#  3.  fist_name[0:6:1]   yaha 6 ya len(fist_mane) ye bata hai ki kaha tak sring chahiye 
#  4.  fist_name[0:6:1]  or final 1 ka matal ye hai ki kitna kitna gap ke bad sring chahiye matalb jaise c programing me pade hai i++


#Type Conversion
# You can convert a value from one type to another using these built-in functions: Examples
age = 21.5;    # it float data type the convart the ins data type matalb intages 
print(str(age));  
age_str =  str(age);
print(type(age_str))   # output 21

last_name = "10";
print(type(last_name));
print(int(last_name));

# matalb samjho  kiska valu kime convart hoga 
# int ->  <- float 
# str (Sting) <- int or float domo me  but 
# int or float ka bhi Srt me change nahi ho payega 
# impotent baat samjho Type Conversion me 7 aayese valu hota hai liska bool matal boolean false hota hai 
# Everything converts to True with bool() — except these 7 values which become False:
#   0, 0.0, False, "", [], {}, ()

 



   







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






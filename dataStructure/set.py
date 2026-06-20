# Set — Unique Values Only
# ab samjhte hai ki ye Unique Values kya hota hai matalb samjho jo Unique Value repled value nahi hota hai 


# matalb samjho Example

# a = {1, 2, 3, 4, 5, 6, 7, 4, 4, 3, 6, 9}  # set ko hm {} bricet me likhte hai
# uniq_value = set(a) 
# print(uniq_value)
# #print(uniq_value[0])  #error dega kyu ki hm set ko index se exace nahi kar payenge

# # ye dobul value ko jitna bhi hota hai use.

# # look impliment
# for i in a:
#     print(i)

# mathmetic opraton on set

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}


# ye sabhi opration 11th math me padhe honge 
print(a | b)   # Union         → {1,2,3,4,5,6}
print(a & b)   # Intersection  → {3,4}
print(a - b)   # Difference    → {1,2}
print(a ^ b)   # Symmetric diff→ {1,2,5,6}


# A set automatically removes duplicates and has no guaranteed order. 
# Great for checking membership and performing math-style set operations.


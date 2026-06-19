# Q1. Print all positive and negative elements separately.
# Input: [3, -1, 4, -5, 9]
# Positive: [3,4,9] Negative: [-1,-5]


# a = [3, -1, 4, -5, 9]

# pos = []
# neg = []

# for i in a:
#     if i >= 0:
#         pos.append(i)
#     else:
#         neg.append(i)

# print(f"this are posetive numer {pos}")
# print(f"this are posetive numer {neg}")

# ise function se kaise banaye 

# pos = []
# neg = []

# def num(b):    # paramitar
#     for i in b:
#         if i <= 0:
#             pos.append(i)
#         else:
#             neg.append(i)


# b = [2, -1 , 0 , -4, 9, -56]    # Argument the 

# num(b)   # call the function 


# print(f"this are posetive numer {pos}")   # print the function
# print(f"this are posetive numer {neg}")



#Q2 Find the mean (average) of all list elements.
# Input: [10, 20, 30, 40]
# Mean = 25.0

# samjho Average kya hota hai = total numabr ka sum /total numabr or object matal leg() function ka user sb samjhate hai 


a = [10, 20, 30, 40]
sum = 0
avr = 0

for i in a:
    sum = sum + i


print(f"after sum is total sum {sum}")
avr = sum/len(a)

print(f"aftar Avreges is a {avr}")

# ab ise function se banayenge 

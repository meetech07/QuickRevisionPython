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


# a = [10, 20, 30, 40]
# sum = 0
# avr = 0

# for i in a:
#     sum = sum + i


# print(f"after sum is total sum {sum}")
# avr = sum/len(a)

# print(f"aftar Avreges is a {avr}")

#    __________________ab ise function se banayenge _______________________________________
sum = 0
avg = 0 

# def avreg(a):
#     global sum  # ab hm function ke bahar excex kar payenge.
#     global avg
#     # sum = 0
#     # avg = 0
#     for i in a:
#         sum = sum + i
#     print(f"the total sum is {sum}")
#     avg = sum/len(a)
#     print(f"total average is a {avg}")


# user_input_list = input("entar the list of num ") # a of agument of the value
# a = list(map(int, user_input_list.split()))   # map()  method me baad me dekhenge jb advance function padenge
# avreg(a)    # call the function


# print(sum)   # ise hm bahar exace nahi kar payenge kyu ki ek ye function ke andar hai matal ushka scop ush function tak simit rahega 
# print(avg)   # ise hm bahar exace nahi kar payenge kyu ki ek ye function ke andar hai matal ushka scop ush function tak simit rahega 

# gar hamko globul exacexe karna hai to hamko function ko batana padega ki ye variabul jo hm glopli user karenge matalb samjho ham use pure code me kahi bhi user kar sakte hai 


#  Q3. Find the greatest element and print its index.
# Input: [4, 8, 2, 9, 1]
# Greatest = 9 at index 3


# pahle samjhte hai ki kya karna hai hame ek pure lish me se ek element nikalna hai jo sab se bada hai or ushka index bhi find karna hai pahle bina function ke samjhate hai.

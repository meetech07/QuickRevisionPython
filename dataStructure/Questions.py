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
# sum = 0
# avg = 0 

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

# print("intar the fist no. and space nest second numaber or th space")
# user_input_numars = input("entar the list-: ") 
# a = list(map(int, user_input_numars.split()))   # map hm age padenge
# print(a)  # mere pass list or "a" aa gya hai 

# gret_indexs = 0

# for i in range(len(a)-1):
    # if a[i] > gret:
    #     gret = a[i]
    #     gret_indexs = i
# print(f"the gretes no. is {gret} and the index {gret_indexs} ")

# function ka user karte hai.
# def greted(a):
#     gret = a[0]
#     global gret_indexs
#     for i in range(len(a)-1):
#         if a[i] > gret:
#             gret = a[i]
#             gret_indexs = i
#     print(f"the all lish is greted numaber is {gret} or ushki index {gret_indexs}")

# print("intar the fist no. and space nest second numaber or th space")
# user_input_numars = input("entar the list-: ") 
# a = list(map(int, user_input_numars.split()))   # map hm age padenge

# greted(a)


# ab hm do inbilde function ka user kar ke gretest numaber nikalenge or index bhi.
# pahle function pure list me se maxmum numar max() methode se nikalenge.

# l = [4, 8, 2, 9, 1]

# greted_bject_of_list = max(l)  # yaha se mere ko bada numabe mil jayga.

# gretest_index_of_list = l.index(greted_bject_of_list) # hame ush number ka index mil jayega 

# print(f"the gretes number is {greted_bject_of_list} and index of {gretest_index_of_list}")


# Q4 Find the second greatest element.
# Input: [4, 8, 2, 9, 1]
# Second greatest = 8

# solustion. agar mere ko bada num. mil jaye or use hm delect kar de to second bada no. mil jayega 

l = [4, 8, 2, 9, 1, 1, 4]  
indes = 0  # agar ush numar ka index janna hai to

bada_num = max(l)   # ise sab se bad numar aa jayega 
print(bada_num)
# pahle jo bada numabe mere ko mila hai ush list me dekhenge ki koi dobul numare to nahi hai 
# use dekhne ke liye hame set() methaod ka user karna badega 

uniq_numar_of_list = list(set(l))  # ye set kam karega ki jo bhi dobul numar list me hoga use hta dega 
print(uniq_numar_of_list)

uniq_numar_of_list.remove(bada_num)   # AB JO bubale no. hatane ke bad use list me dal lenge or bade numar ko nuw list se delect kar denge 
print(uniq_numar_of_list)

second_numar = max(uniq_numar_of_list)   #ab jo bada no. remov ho gya hai to jo new list bana hai na useke max numar nikal lenge 
seconde_index = l.index(second_numar)

print(f"second greted numabr of {second_numar} or index the {seconde_index} ")


# Q5.Check if the list is already sorted.
# Input: [1, 3, 5, 7]
# List is sorted ✅
# Input: [3, 1, 4]
# Not sorted ❌




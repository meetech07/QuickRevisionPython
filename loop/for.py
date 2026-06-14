# range() function is use the range of matalb ye kaha se lkaha tak jayega 
# range(start,stop,skip) ise hm dekhenge ki kon kya karta hai 

# range(start,stop,skip)  yaha start ka matalb ye hai ki hame kaha se strt karne kaha se karna hai.
# range(start,stop,skip) or yaha stop ka matalb ye hai ki hmara range kaha rukna chahiye.
# range(start,stop,skip) or skip ya jump ka matalb ye hai ki ek or dusre ke bich kiyna juam ya gap hona chahiye.
# ab example dekhte hai.

# range(stop)             # 0 up to stop-1
# range(start, stop)      # start up to stop-1
# range(start, stop, step)# start, jumping by step

for i in range(10,21,1):
    print(i)



# for loop ke andar bhi break aur continue ka use hota hai

for i in range(1,10):
    if i == 5:
        break
    print(i)

#continua example
for i in range(1,10):
    if i == 5:
        continue
    print(i)

    # Questions

# 1. Write a for loop that prints the numbers from 1 to 10.
for i in range(1,11):
    print(i)

 # 2. Write a for loop that prints the even numbers from 1 to 20.
for i in range(2,21,2):
    print(i)


# 3. Write a for loop that prints the odd numbers from 1 to 20
for i in range(1,21,2):
    print(i)

# 4. Write a for loop that prints the squares of the numbers from 1 to 10.
for i in range(1,11):
    print(i**2)

# nid levar questionce

#5. Write a for loop that prints the first 10 Fibonacci numbers.
a, b = 0, 1
for i in range(10):
    print(a)
    a, b = b, a + b


# 6. Write a for loop that prints the multiplication table of 5.

# ki file se data ko kaise late hai 

# f = open("dia.txt", "w")
# data = input("tum yaha aapne EX ki yaad likh sakte ho:- ")

# f.write(data)  # yaha par hm jo file banaye hai use f variyablum me save kiye hai  write se ush file me data ko bheje hai

#  ush file ko read kar sakte hai
# f2 = open("dia.txt", 'r')
# print(f2.read())


# f2 = open("dataStructure\set.py", 'r')
# print(f2.read())

# f2 = open("dia.txt", 'a')

# d2 = input("add the informetion:- ")
# f2.write(d2)

# r1 = open("dia.txt", 'r')
# print(r1.read())


# Always use the
# with
# statement — it automatically closes the file for you, even if an error occurs.

with open("dia.txt",'r') as f:
    r =  f.read()
    print(r)


# Writing
with open("notes.txt", "w") as f:
    f.write("Hello from Python!")

# Reading
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)

# Appending
with open("notes.txt", "a") as f:
    f.write("\nAdded a new line!")

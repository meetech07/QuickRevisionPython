# -----------------Key-Value Storage-----------------------------------
#A dictionary stores data as key: value pairs — like a real dictionary where you look up a word (key) to find its meaning (value).
# key       key    Value     key  Value  key     Value
# person = {"name": "Akarsh", "age": 20, "city": "Indore"}

# # key like dinoted by cosmaizetion index 
# # yaha key ka bs etna sa matalb hai ki hm khud se index ke value de sakte hai 


# # Read
# print(person["name"])        # Akarsh

# # Update
# person["age"] = 21

# # Add new key
# person["course"] = "Python"

# # Delete
# del person["city"]

# # Traverse
# for key, val in person.items():
#     print(key, "→", val)





# Question

# Q1 Merge two dictionaries into one.
# d1={a:1}, d2={b:2}
# {a:1, b:2}  this output 

d1={"a":1}
d2={"b":2}

print(hash(d1))
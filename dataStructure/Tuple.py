# tuole data  in bulde structure on python
# Tuple — The Immutable List  matalb kisi bhi index ke value ko change nahi kiya ja sakta hai
# ise likhne ka tarika 


#index    0      1      2
days = ("Mon", "Tue", "Wed")   # ise hm () bricet me likhte hai
# value   Mon    Tue   Wed

print(type(days))    # tuple 

print(days[0])   # Mon

# days[0] = "X"   # ❌ TypeError — tuples are immutable


# METHOD

# FIST MEDHOD hm kisi bhi value ka index dekh skte hai 
print(days.index("Tue"))

# second method it's count

print(days.count("Mon"))  # count kya karta hai ye pure tuplu me khojta hai ki koi number kitna nar aya hai

# loop kaise apply hota hai 
a = (1, 2, 3, 4, 5, 6, 5, 4, 5, 6)
for i in a:
    print(a[i])
# Conditional Statements
# Making Decisions in Code
# Real programs don't run the same code every time — they make decisions.
# Conditional statements let your program choose what to do based on a condition. That's why they're also called control flow statements.

# if condition:
#     # runs when condition is True
# elif another_condition:
#     # runs if the above was False, this is True
# else:
#     # runs when nothing above was True


# Ab matalb samjho if ka agar koi condiction trua hoga tab hi ye condiction chalega 
# ab else ka matalb samjho agr if ka condiction nai chala to ye chalega 
# ab elif ka matab samjho koi condiction if ka nahi cla to else se pahle ye condiction chaleg aao samjhte hi examples se.

if 5 > 7:              # pahle ye line chalega jb ye true ho jayega to code excuted ho jayega or niche wala condiction check nahi ho payega
    print("5 is greater than 3");
elif 3 < 2:         # agar if ka codiction fales hoga tb hi elif ka condiction chalega 
    print("2 is greaters then 3" );
else:   # ahar koi condiction nahi chala to else chalega 
    print("then no true any number");
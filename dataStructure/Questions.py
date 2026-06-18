# Q1. Print all positive and negative elements separately.
# Input: [3, -1, 4, -5, 9]
# Positive: [3,4,9] Negative: [-1,-5]


a = [3, -1, 4, -5, 9]

pos = []
neg = []

for i in a:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)

print(f"this are posetive numer {pos}")
print(f"this are posetive numer {neg}")





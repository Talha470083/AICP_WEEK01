names = []
weights = []
default_name = "No Name"
default_weight = "0"
i = 0

while i < 30:
    print("Enter the name of Student:")
    n = input()

    if n not in names:
        names.append(n)
    else:
        names.append(default_name)

    print("Enter the weight of Student in KG's:")
    w_str = input()

    if w_str.isdigit() and float(w_str) >= 19 and float(w_str) <= 80:
        weights.append(float(w_str))
    else:
        weights.append(default_weight)


    i += 1
print("---------------------AT THE BEGINING OF TERM------------------------")
for i in range(len(names)):
    print(f"{names[i]}, {weights[i]} kg")

















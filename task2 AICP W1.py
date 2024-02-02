# Collect weights at the end of term and calculate the difference
weight_endterm = []
difference = []

print("\n---------------------AT THE END OF TERM------------------------")
for i in range(len(names)):
    print(f"Enter the weight of {names[i]}:")
    while True:
        w_str = input()
        try:
            weight = float(w_str)
            if 19 <= weight <= 80:
                weight_endterm.append(weight)
                difference.append(weights[i] - weight)
                break
            else:
                print("Weight must be between 19 and 80 kg.")
        except ValueError:
            print("Invalid input. Please enter a valid weight.")

# Display names, weights of those exceeding 2.5 KGs at the end of term,
print("\n---------------------AT THE END OF TERM------------------------")
for i in range(len(difference )):
    if difference[i]>2.5:
         print(f"{names[i]} has gained weight around {difference[i]} kg")



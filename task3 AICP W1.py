# Display names, weights of those exceeding 2.5 KGs at the end of term,
print("\n---------------------AT THE END OF TERM------------------------")
for i in range(len(difference )):
    if difference[i]>2.5:
         print(f"{names[i]} has gained weight around {difference[i]} kg")

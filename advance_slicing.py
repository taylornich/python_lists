# question 3 task 1

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

week2_temps = temperatures[7:14]

print(week2_temps)

# question 3 task 2
temp_over_100 =[]

for i in temperatures:
    if i > 100:
        temp_over_100.append(i)

print(temp_over_100)

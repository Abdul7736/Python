attendance = [18, 20, 19, 15, 21]
full_days = 0
total_attendance = 0
for day in attendance:
    if day >= 20:
        print(day, "Full")
        full_days += 1
    else:
         print(day, "Not Full")
    total_attendance += day
print("Number of full days:", full_days)
print("Total attendance over the week:", total_attendance)
        
        
        

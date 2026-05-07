academic_score = float(input("Enter the academic score:"))
attendance_percentage = float(input("Enter the attendance percentage:"))
extracurricular_activities = input("Do you have extracurricular activities? (yes/no):").lower()
if academic_score >=60 and attendance_percentage >= 75 and extracurricular_activities == "yes":
    print(f"Congratulations! You are eligible for the interview.")
else:
    print("Sorry, you are not eligible for the interview.") 
        

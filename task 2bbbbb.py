def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! 🌟 Keep shining!"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good effort! You can do even better 😊"
    elif marks >= 60:
        return "D", "You passed! Work harder next time 💪"
    else:
        return "F", "Don't lose hope! Practice makes perfect 🌱"


name = input("Enter student name: ")

while True:
    marks = int(input("Enter marks (0-100): "))
    
    if 0 <= marks <= 100:
        break
    else:
        print("❌ Invalid marks! Please enter marks between 0 and 100.")

grade, message = calculate_grade(marks)

print("\n📊 RESULT FOR", name.upper())
print("Marks:", marks, "/100")
print("Grade:", grade)
print("Message:", message)

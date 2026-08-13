
print("Enter your English marks")
user_input1 = int(input())
print("Enter your Hindi marks")
user_input2 = int(input())
print("Enter your science marks")
user_input3 = int(input())
print("Enter your math marks")
user_input4 = int(input())
print("Enter your computer marks")
user_input5 = int(input())
print("Enter your Social studies marks")
user_input6 = int(input())

total_marks = user_input1 + user_input2 + user_input3 + user_input4 + user_input5 + user_input6
percentage = total_marks / 6

print("Total marks:", total_marks)
print("Percentage:", percentage)

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 50:
    grade = "E"
else:
    grade = "Fail"

print("Grade:", grade)
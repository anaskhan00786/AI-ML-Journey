print("enter your number")
user_input1=int(input())
if (user_input1>0):
    print("positive ")


print("Enter a number")
user_input2=int(input())
if(user_input2%2==0):
    print("even")
else:
    print("odd")

print("enter two numbers")
user_input3=int(input())
user_input4=int(input())
if (user_input3>user_input4):
    print(f"{user_input3} is greater than {user_input4}")
else:
    print(f"{user_input4} is greater than {user_input3}")


print("enter your age")
age=int(input())
if (age<13):
    print("your a child")
elif(age>=13 and age<19):
    print("your a teenager")
elif(age>19 and age<=59):
    print("your a adult")
else:
    print("your a senior citizen")

print("Enter your user name and password")
correct_username = "admin"
correct_password = "python123"
user_input5=str(input())
user_input6=str(input())

if(correct_username==user_input5 and correct_password==user_input6):
    print("login successfull")
else:
    print("login failed")
    print("enter correct password and username")

    
    
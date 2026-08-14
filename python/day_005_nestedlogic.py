user_input1=int(input("Enter a number:"))
user_input2=int(input("Enter a number:"))
user_input3=int(input("Enter a number:"))
if(user_input1>user_input2 and user_input1>user_input3):
    print("user_input1 is largest")
elif(user_input2>user_input1 and user_input2>user_input3):
    print("user_input2 is largest")
else:
    print(f"{user_input3} is largest")


even_count = 0
odd_count = 0

# Loop 8 times to get 8 numbers
for i in range(8):
    num = int(input(f"Enter number {i+1}: "))
    
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("---")
print(f"Total Even Numbers: {even_count}")
print(f"Total Odd Numbers: {odd_count}")

for i in range(1,11):
    user=int(input("Enter a number:"))
    table=user*i
    print(table)
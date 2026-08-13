for i in range(10):
    if i==2:
        continue
    print(i * "*")
    i=i+1


    
for i in range(0,50,2):
    print(i)


print("enter a number")
user_input1=int(input())
i=1
while i<=10:
    print(i*user_input1)
    i=i+1
    


user_input=int(input("enter a number"))
total=0
for i in range(1,user_input+1):
    total=total+i
print(total)
    
user_input=input("Eneter a string: ")
count=0
for character in user_input:
    count=count+1
print(count)
    
    
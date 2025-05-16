age = int(input("Enter your age:"))

if(age>18):
    print("You can drive ")
elif(age==18):
    print("You need to schedule a interview")
elif(age == 0):
    print("You have born today")
else:
    print("You cannot drive")
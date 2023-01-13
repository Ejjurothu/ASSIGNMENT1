#read the score from users
rlt=int(input("enteryour result"))
#using if condition ,"and-operator" and  comparison operators to compare the score ,disply the result using print function

if(rlt>=90 and rlt<=100):
    print("your grade is A")
elif(rlt>=80 and rlt<=89):
    print("your grade is B")
elif(rlt>=70 and rlt<=79):
    print("your grade is C")
elif(rlt>=60 and rlt<=69):
    print("your grade is D")
elif(rlt>=0 and rlt<=59):
    print("your grade is F")
#logical operator
citizenship=input("enter citizenship").lower()
age=int(input("Enter the age:"))
if citizenship=="kenyan"and age>=18:
  print("eligible")
else:
  print(" Not eligible")
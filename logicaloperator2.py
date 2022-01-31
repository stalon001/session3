print('Hello, world!')
citizenship=input("enter citizenship").lower()
age=int(input("Enter the age:"))
country=["kenya","uganda","tanzania"]
if citizenship in country and age>=18:
 print("eligible")
else:
 print("Not eligible")
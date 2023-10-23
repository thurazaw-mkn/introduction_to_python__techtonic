grade = int(input("Enter your grade"))


if grade >= 90:
	print("Congratulations!!!")
	print("You passed the exam with A")
elif grade >=80:
	print("Congratulations!")
	print("You passed the exam with B")
elif grade >=60:
	print("You passed the exam with C")
elif grade >=40:
	print("You passed the exam with D")
else:
	print("Try again!")
	print("You failed the exam!!")
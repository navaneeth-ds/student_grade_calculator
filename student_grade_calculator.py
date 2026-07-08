name = input("Enter student name:")
marks = []

mark1 = int(input("Enter first mark:"))
marks.append(mark1)

mark2 = int(input("Enter second mark:"))
marks.append(mark2)

mark3 = int(input("Enter third mark:"))
marks.append(mark3)

print(marks)
sum(marks)
len(marks)
average = sum(marks)/len(marks)
print("average marks:",sum(marks)/len(marks))

if average >= 90:
  print("Grade A")
elif average >= 75:
  print("Grade B")
elif average >= 50:
  print("Grade C")
else:
  print("Fail")

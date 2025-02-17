"""Q.3 A teacher maintains a list of students in a class. The list is ["Alice", "Bob", "Charlie",
"David", "Eve"]. Write a Python program to print the names of students whose names start
with "A" or "D"."""

student_name_list = ["Alisa", "Bob", "Charlie", "David", "Eve"]

for i in student_name_list:
    if i.startswith("A") or i.startswith("D"):
        print(i)
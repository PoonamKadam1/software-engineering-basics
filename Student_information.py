student = {}

student["name"] = input("Enter name: ")
student["age"] = input("Enter age: ")
student["degree"] = input("Enter degree: ")

print("\nStudent Profile")
for key, value in student.items():
    print(key, ":", value)

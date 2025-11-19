
student = {
    "name": "Alice",
    "age": 20,
    "courses": ["Math", "Physics"]
}


print("Name:", student["name"])
print("Age:", student.get("age"))


student["email"] = "alice@example.com"
student["age"] = 21


for key, value in student.items():
    print(key, ":", value)


student.pop("courses")
print("After removal:", student)

students = {
    "s1": {"name": "Alice", "age": 20},
    "s2": {"name": "Bob", "age": 22}
}

print("Student s2 name:", students["s2"]["name"])

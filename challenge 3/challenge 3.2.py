class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the list of student objects based on their CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of student objects
if __name__ == "__main__":
    students1 = [
        Student("Alice", "A123", 3.8),
        Student("Bob", "B456", 3.6),
        Student("Charlie", "C789", 4.0),
    ]

    students2 = [
        Student("David", "D101", 3.9),
        Student("Eve", "E202", 3.7),
        Student("Frank", "F303", 3.5),
    ]

    sorted_students1 = sort_students(students1)
    sorted_students2 = sort_students(students2)

    print("Sorted Students 1:")
    for student in sorted_students1:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")

    print("\nSorted Students 2:")
    for student in sorted_students2:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")

# Create a list to store our students
students = []

while True:
    # Get student information
    print("\nEnter student ID:")
    student_id = input()
    
    print("Enter number of books purchased:")
    books_purchased = int(input())
    
    # Calculate points based on books purchased
    if books_purchased >= 8:
        points = 60
    elif books_purchased == 6:
        points = 30
    elif books_purchased == 4:
        points = 15
    elif books_purchased == 2:
        points = 5
    else:
        points = 0
    
    # Store the student record
    student_record = {
        "student_id": student_id,
        "books": books_purchased,
        "points": points
    }
    students.append(student_record)
    
    # Ask if we should continue
    print("\nAdd another student? (yes/no)")
    if input().lower() != 'yes':
        break

# Display all records
print("\nAll Student Records:")
print("-------------------")
for student in students:
    print(f"Student ID: {student['student_id']}")
    print(f"Books Purchased: {student['books']}")
    print(f"Points Earned: {student['points']}")
    print("-------------------")
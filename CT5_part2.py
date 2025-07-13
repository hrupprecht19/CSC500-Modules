students = [ ]
#thinking the book club would use the student ID for points
while True:
  #get the student information
  print("\nEnter student ID:")
  student_id = input ()
  
  print("Enter number of books purchased:")
  books_purchased = int(input())

  #calculate 
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

    student_record = {
      "student_id": student_id,
      "books" : books_purchased,
      "points" : points
    }
    student.append{student_record)
                   


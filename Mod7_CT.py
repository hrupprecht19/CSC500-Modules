class CourseInfo:
    def __init__(self):
        # Initialize the course information dictionary
        self._course = {
            "CSC101": ["3004", "Hayes", "8:00 AM"],
            "CSC102": ["4501", "Alvarado", "9:00 AM"],
            "CSC103": ["6755", "Rich", "10:00 AM"],
            "NT110": ["1244", "Burke", "11:00 AM"],
            "CM241": ["1411", "Lee", "1:00 PM"]
        }
# This is to ensure the course information is private and not directly accessible
    def display_course_info(self, course_number):
        course_info = self._course.get(course_number)
        if course_info is None:
            print(f"\nError: Course '{course_number}' not found. Please enter a valid course number.")
            return
        # Display the course information
        print(f"\nCourse Information for {course_number}:")
        print(f"Room: {course_info[0]}")
        print(f"Instructor: {course_info[1]}")
        print(f"Time: {course_info[2]}")
# This is the main function to run the program
def main():
    courses = CourseInfo()
    # Main loop to get user input for course numbers
    print("Welcome to the Course Information System!") 
    print("Type 'quit' to exit the program.")
    print("Please enter a course number to get its information.\n")
    # Loop to continuously ask for course numbers until 'quit' is entered
    while True:
        # Prompt the user for a course number
        print("\nEnter course number :")
        course = input().upper().strip()
        if course == 'QUIT':
            print("Goodbye!")
            break
        if not course.isalnum():
            print("Error: Invalid input. Please enter a valid course number (letters and numbers only).")
            print("Available courses: CSC101, CSC102, CSC103, NT110, CM241")
            continue
        courses.display_course_info(course)

if __name__ == "__main__":
    main()
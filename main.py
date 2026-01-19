class Course: 
    FILE = "courses.txt" 
        
    @staticmethod 
    def add_courses(): 
        course_id = input("Enter course id: ").strip()
        course_name = input("Enter course name: ").strip()

        with open(Course.FILE, "a") as file: 
            file.write(f"{course_id},{course_name} \n") 

        print("Course added successfully!\n")
            
    @staticmethod 
    def show_all_courses(): 
        course_list = [] 

        try:
            with open(Course.FILE, "r") as file: 
                for course in file: 
                    course = course.strip()
                    if not course:
                        continue


                    course_part = course.split(",")
                    if len(course_part) !=2 :
                        continue

                    course_list.append((course_part[0], course_part[1])) 

        except FileNotFoundError:
            pass

        return course_list
    
    @staticmethod
    def get_all_course_ids():
        return [course_id for course_id, _ in Course.show_all_courses()]



class Student:
    FILE = "students.txt"


    def __init__(self, student_roll, student_name, student_password, course_list=None):
        self.student_roll = student_roll
        self.student_name = student_name
        self.__student_password = student_password
        self.course_list = course_list if course_list else []


    def get_password(self):
        return self.__student_password
    

    def save(self):
        courses_str = "|".join(self.course_list)
        with open(Student.FILE, "a") as file:
            file.write(f"{self.student_roll}, {self.student_name},{self.__student_password}, {courses_str}\n")


    @staticmethod
    def add_student():
        student_roll = input("Enter roll: ").strip()
        student_name = input("Enter name: ").strip()
        student_password = input("Enter password: ").strip()
        courses_input = input("Enter course ids (use | between courses, e.g. CSE101|CSE102): ").strip()
        

        input_courses = courses_input.split("|") if courses_input else []
        valid_courses = Course.get_all_course_ids()
        enrolled_courses = []
        invalid_courses = []

        enrolled_courses = []
        invalid_courses = []

        for course in input_courses:
            if course in valid_courses:
                enrolled_courses.append(course)
            else:
                invalid_courses.append(course)

        if invalid_courses:
            print("This course don't opened evet:", ", ".join(invalid_courses))
            print("Student Add Failed! \n")
            return
        

        student =  Student(
            student_roll, 
            student_name, 
            student_password, 
            enrolled_courses
        )
        student.save()

        print("Student added successfully!\n")


    @staticmethod
    def show_all_students():
        student_list = []

        try:

            with open(Student.FILE, "r") as file:
                for student_row in file:
                    student_row = student_row.strip()

                    if not student_row:
                        continue
                    
                    student_data_part = student_row.split(",")

                    if len(student_data_part) != 4:
                        continue

                    student_roll, student_name, student_password, courses = student_data_part
                    course_list = courses.split("|") if courses else []
                    student = Student(student_roll, student_name, student_password, course_list)
                    student_list.append(student)
        
        except FileNotFoundError:
            pass
        return student_list




while True:
    print("*************< Main Menu >*************")
    print("1. Add Course")
    print("2. View All Course")
    print("3. Add New Courses")
    print("4. View All Student")
    print("5. Exit")


    option = input("Enter your choice: ").strip()

    if option == "1":
        Course.add_courses()

    elif option == "2":
        print("\n*************< Course List >*************")
        print("\n")
        for CourseId, CourserName in Course.show_all_courses():
            print(CourseId, "-", CourserName)
        print("\n")

    elif option == "3":
        Student.add_student()

    elif option == "4":
        print("\n*************< Student List >*************")
        print("\n")
        for i, stu in enumerate(Student.show_all_students(), start=1):
            print(
                f"{i}. Roll: {stu.student_roll} | "
                f"Name: {stu.student_name} | "
                f"Courses: {stu.course_list} | "
                f"Password: {stu.get_password()}"
            )
        print("\n")

    elif option == "5":
        print("Program exited.")
        break

    else:
        print("Sorry Invalid choice!\n")
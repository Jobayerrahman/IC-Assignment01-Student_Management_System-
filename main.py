class Course: 
    FILE = "courses.txt" 

    def __init__(self,course_name,course_id): 
        self.course_name = course_name 
        self.course_id = course_id 
        
    @staticmethod 
    def create_courses(course_id, course_name): 
        with open(Course.FILE, "a") as file: 
            file.write(f"{course_id},{course_name} \n") 
            
    @staticmethod 
    def get_all(): 
        course_list = [] 
        with open(Course.FILE, "r") as file: 
            for course in file: 
                course = course.strip()
                if not course:
                    continue


                parts = course.split(",")
                if len(parts) !=2 :
                    continue

                course_id, course_name = parts
                course_list.append((course_id, course_name)) 
        return course_list



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
        courses = "|".join(self.course_list)
        with open(Student.FILE, "a") as file:
            file.write(f"{self.student_roll}, {self.student_name},{self.__student_password}, {courses}\n")

    @staticmethod
    def get_all_students():
        student_list = []

        with open(Student.FILE, "r") as file:
            for line in file:
                student_roll, student_name, student_password, courses = line.strip().split(",")
                course_list = courses.split("|") if courses else []
                student = Student(student_roll, student_name, student_password, course_list)
                student_list.append(student)
        return student_list


Course.create_courses("course-1001","Python") 
Course.create_courses("course-1002","SQL") 

s1 = Student(1, "Rahim", "pass123", ["CSE101", "CSE102"])
s2 = Student(2, "Karim", "abc456", ["CSE101"])

s1.save()
s2.save()



print("------ Course Information ------") 
for course_id, course_name in Course.get_all():
    print(course_id, course_name)
print("------ Course End ------") 


print("\n")



students = Student.get_all_students()
print("------ Student Information ------")
for stu in students:
    print("Roll:", stu.student_roll)
    print("Name:", stu.student_name)
    print("Courses:", stu.course_list)
    print("Password:", stu.get_password())

print("------ Student End ------")
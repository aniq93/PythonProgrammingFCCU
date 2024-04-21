class Course:

    def __init__(self,c_name,c_code,teacher):
        self.course_name = c_name
        self.corse_code  = c_code
        self.instructor = teacher
        self.students  = []

    def addStudent(self,student):
        
        self.students.append(student.f_name) 
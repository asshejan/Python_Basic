class Student:
    def __init__(self, name, cls,  id):
        self.name = name
        self.id = id
        self.cls = cls

    def __repr__(self) -> str:
        return f'name is {self.name} id is {self.id} class is {self.cls}'

class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher name is {self.name} and teaches {self.subject} and id is {self.id}'
    

class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee<6500:
           return 
        else:
           id = len(self.students) +1
           student = Student(name, 'C', id)
           self.students.append(student)

    def __repr__(self) -> str:
        print('Welcome to ', self.name)
        print('________Our Teacher________')
        for teacher in self.teachers:
            print(teacher)
        print('________Our Students________')
        for student in self.students:
            print(student)



shejan = School('SHEJAN')
shejan.enroll('Alia', 6500)
shejan.enroll('Samia', 6700)
shejan.add_teacher('Rahim Sir', 'Math')
shejan.add_teacher('Karim sir', 'English')

print(shejan)
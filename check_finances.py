class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."


class Employee(Person):
    def __init__(self, name, age, rate, number_of_hours):
        Person.__init__(self, name, age)
        self.rate = rate
        self.number_of_hours = number_of_hours

    def show_finance(self):
        return self.rate * self.number_of_hours

    def speak(self):
        print(f"I am an employee, my name is {self.name}!")


class Student(Person):
    def __init__(self, name, age, scholarship):
        Person.__init__(self, name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship

    def speak(self):
        print(f"I am a student, my name is {self.name}!")


class WorkingStudent(Student, Employee):
    def __init__(self, name, age, rate, number_of_hours, scholarship):
        Employee.__init__(self, name, age, rate, number_of_hours)
        Student.__init__(self, name, age, scholarship)

    def show_finance(self):
        return self.rate * self.number_of_hours * self.scholarship

def check_finance(person_obj):
    print(person_obj.show_finance())


ws1 = WorkingStudent("Alex", 23, 20, 16, 1000)
print(ws1)
ws1.speak()
print(ws1.show_finance())
print(WorkingStudent.__mro__)

person = Person("Bianca", 25)
print(person)

employee = Employee("Ion", 27, 30, 1600)
employee.speak()

student = Student("Maria", 20, 600)
student.speak()

print("Checking finances for employee")
check_finance(employee)

print("Checking finances for student")
check_finance(student)

print("Checking finances for working student")
check_finance(ws1)
class Student:
    def __init__(self, name, fee):
        self.name = name
        self.fee = fee

    def display_fee(self):
        print(f"{self.name} needs to pay: ${self.fee}")

class ScholarshipStudent(Student):
    def __init__(self, name, fee, discount):
        super().__init__(name, fee)
        self.discount = discount

    def display_fee(self):
        final_fee = self.fee - self.discount
        print(f"{self.name} (Scholarship) needs to pay: ${final_fee}")


regular_student = Student("John", 1000)
special_student = ScholarshipStudent("Sarah", 1000, 300)

regular_student.display_fee() 
special_student.display_fee()
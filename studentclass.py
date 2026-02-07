class Student:
    def __init__(self, name, student_id, grades):
        self.name = name            
        self.student_id = student_id 
        self.grades = grades        

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        avg = self.calculate_average()
        print(f"Student: {self.name} (ID: {self.student_id})")
        print(f"Average Grade: {avg:.2f}")

student1 = Student("Alice Smith", "S101", [85, 90, 78])
student2 = Student("Bob Jones", "S102", [70, 65, 80])

student1.display_info()
student2.display_info()
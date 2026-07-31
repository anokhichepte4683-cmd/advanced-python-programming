# Decorator to add a report header
def report_header(func):
    def wrapper(*args, **kwargs):
        print("=" * 40)
        print("         STUDENT REPORT")
        print("=" * 40)
        func(*args, **kwargs)
        print("=" * 40)
    return wrapper


class Report:
    college = "MIT ADT University"

    # Constructor (Magic Method)
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    # Class Method
    @classmethod
    def change_college(cls, new_name):
        cls.college = new_name

    # Magic Method
    def __str__(self):
        return f"Name : {self.name}\nRoll No : {self.roll}\nMarks : {self.marks}"

    # Decorator applied to display report
    @report_header
    def display_report(self):
        print(f"College : {Report.college}")
        print(self)
        if self.marks >= 40:
            print("Result : PASS")
        else:
            print("Result : FAIL")


# Main Program

student1 = Report("Anokhi", 7, 91)
student1.display_report()
print()

Report.change_college("Pune Institute of Computer Technology")

student2 = Report("Vaishnavi", 52, 45)
student2.display_report()

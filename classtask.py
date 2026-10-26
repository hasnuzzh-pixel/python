class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks= marks

    def display_grade(self):
        if self.marks >= 90:
            grade = "A"
        elif self.marks >= 75:
            grade = "B"
        elif self.marks >= 50:
            grade = "C"
        else:
            grade = "FAIL"

        print(f"{self.name}'s grade: {grade}")

student1 = student("shahana" ,80)
student2 = student("aswathy",95)


student1.display_grade()
student2.display_grade()
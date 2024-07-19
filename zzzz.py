class Student:
    auto_increment_id = 1  # Variabel kelas untuk auto increment student ID

    def __init__(self, name):
        self.id = Student.auto_increment_id  # Set student ID
        Student.auto_increment_id += 1  # Increment student ID untuk student berikutnya
        self.name = name
        self.scores = []

    def addGrade(self, grade):
        self.scores.append(grade)

    def getAverage(self):
        if len(self.scores) == 0:
            return 0
        return sum(self.scores) / len(self.scores)

    def __str__(self):
        return f"Name: {self.name} Nilai: {self.getAverage():.2f}"



# Contoh penggunaan
student1 = Student("Alice")
student2 = Student("Bob")

student1.addGrade(90)
student1.addGrade(80)
student1.addGrade(85)

student2.addGrade(75)
student2.addGrade(95)

print(student1)  # Output: Name: Alice Nilai: 85.00
print(student2)  # Output: Name: Bob Nilai: 85.00



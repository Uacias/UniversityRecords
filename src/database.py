import json

from src.student import Student


class Database:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.students = [Student.from_dict(item) for item in data]
        except FileNotFoundError:
            print(f"Plik {self.filename} nie istnieje. Tworzenie nowej bazy danych.")
            self.students = []
        except json.JSONDecodeError:
            print("Błąd: Plik JSON jest uszkodzony.")
            self.students = []

    def save(self):
        with open(self.filename, "w") as file:
            json.dump([student.to_dict() for student in self.students], file, indent=4)

    def add_student(self, student):
        self.students.append(student)
        self.save()

    def remove_student(self, index_number):
        self.students = [
            student for student in self.students if student.index_number != index_number
        ]
        self.save()

    def get_all_students(self):
        return self.students

import json

from src.pesel import validate_pesel
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
        if not validate_pesel(student.pesel):
            print("Błąd: PESEL jest nieprawidłowy.")
            return
        self.students.append(student)
        self.save()

    def remove_student(self, index_number):
        self.students = [
            student for student in self.students if student.index_number != index_number
        ]
        self.save()

    def get_all_students(self):
        return self.students

    def find_student_by_last_name(self, last_name):
        return [student for student in self.students if student.last_name == last_name]

    def find_student_by_pesel(self, pesel):
        return next(
            (student for student in self.students if student.pesel == pesel), None
        )

    def sort_students_by_last_name(self, reverse=False):
        self.students.sort(key=lambda student: student.last_name, reverse=reverse)

    def sort_students_by_pesel(self, reverse=False):
        self.students.sort(key=lambda student: student.pesel, reverse=reverse)

    def update_student(
        self,
        index_number,
        new_first_name=None,
        new_last_name=None,
        new_address=None,
        new_pesel=None,
        new_gender=None,
    ):
        if new_pesel and not validate_pesel(new_pesel):
            print("Błąd: PESEL jest nieprawidłowy.")
            return False
        for student in self.students:
            if student.index_number == index_number:
                if new_first_name:
                    student.first_name = new_first_name
                if new_last_name:
                    student.last_name = new_last_name
                if new_address:
                    student.address = new_address
                if new_pesel:
                    student.pesel = new_pesel
                if new_gender:
                    student.gender = new_gender

                self.save()
                return True
        return False

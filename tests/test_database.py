import os
import unittest

from src.database import Database
from src.student import Student


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_database.json"
        self.db = Database(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_and_get_students(self):
        student = Student("John", "Doe", "123 Main St", "12345", "92030512345", "M")
        self.db.add_student(student)

        students = self.db.get_all_students()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].first_name, "John")

    def test_remove_student(self):
        student1 = Student("John", "Doe", "123 Main St", "12345", "92030512345", "M")
        student2 = Student("Jane", "Smith", "456 Elm St", "67890", "85060712345", "F")
        self.db.add_student(student1)
        self.db.add_student(student2)

        self.db.remove_student("12345")
        students = self.db.get_all_students()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].first_name, "Jane")

    def test_save_and_load(self):
        student = Student("John", "Doe", "123 Main St", "12345", "92030512345", "M")
        self.db.add_student(student)

        new_db = Database(self.test_file)
        new_db.load()
        students = new_db.get_all_students()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].first_name, "John")


if __name__ == "__main__":
    unittest.main()

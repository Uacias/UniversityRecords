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
        student = Student("John", "Doe", "123 Main St", "12345", "50121373714", "M")
        self.db.add_student(student)

        students = self.db.get_all_students()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].first_name, "John")

    def test_remove_student(self):
        student1 = Student("John", "Doe", "123 Main St", "12345", "50121373714", "M")
        student2 = Student("Jane", "Smith", "456 Elm St", "67890", "88111919846", "F")
        self.db.add_student(student1)
        self.db.add_student(student2)

        self.db.remove_student("12345")
        students = self.db.get_all_students()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].first_name, "Jane")

    def test_save_and_load(self):
        student = Student("John", "Doe", "123 Main St", "12345", "50121373714", "M")
        self.db.add_student(student)

        new_db = Database(self.test_file)
        new_db.load()
        students = new_db.get_all_students()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].first_name, "John")

    def test_find_student_by_last_name(self):
        student1 = Student("John", "Doe", "123 Main St", "12345", "50121373714", "M")
        student2 = Student("Jane", "Smith", "456 Elm St", "67890", "88111919846", "F")
        self.db.add_student(student1)
        self.db.add_student(student2)

        results = self.db.find_student_by_last_name("Doe")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].first_name, "John")

    def test_find_student_by_pesel(self):
        student1 = Student("John", "Doe", "123 Main St", "12345", "50121373714", "M")
        self.db.add_student(student1)

        student = self.db.find_student_by_pesel("50121373714")
        self.assertIsNotNone(student)
        self.assertEqual(student.first_name, "John")

        student = self.db.find_student_by_pesel("00000000000")
        self.assertIsNone(student)

    def test_sort_students_by_last_name(self):
        student1 = Student("John", "Smith", "123 Main St", "12345", "50121373714", "M")
        student2 = Student("Jane", "Doe", "456 Elm St", "67890", "88111919846", "F")
        self.db.add_student(student1)
        self.db.add_student(student2)

        self.db.sort_students_by_last_name()
        students = self.db.get_all_students()
        self.assertEqual(students[0].last_name, "Doe")
        self.assertEqual(students[1].last_name, "Smith")

    def test_sort_students_by_last_name_desc(self):
        student1 = Student("John", "Smith", "123 Main St", "12345", "50121373714", "M")
        student2 = Student("Jane", "Doe", "456 Elm St", "67890", "88111919846", "F")
        self.db.add_student(student1)
        self.db.add_student(student2)

        self.db.sort_students_by_last_name(reverse=True)
        students = self.db.get_all_students()
        self.assertEqual(students[0].last_name, "Smith")
        self.assertEqual(students[1].last_name, "Doe")

    def test_sort_students_by_pesel(self):
        student1 = Student("John", "Doe", "123 Main St", "12345", "50121373714", "M")
        student2 = Student("Jane", "Smith", "456 Elm St", "67890", "88111919846", "F")
        self.db.add_student(student2)
        self.db.add_student(student1)

        self.db.sort_students_by_pesel()
        students = self.db.get_all_students()
        self.assertEqual(students[0].pesel, "50121373714")
        self.assertEqual(students[1].pesel, "88111919846")

    def test_update_student(self):
        student1 = Student("John", "Doe", "123 Main St", "12345", "50121373714", "M")
        self.db.add_student(student1)

        updated = self.db.update_student(
            index_number="12345",
            new_first_name="Jonathan",
            new_address="New Address 42",
        )
        self.assertTrue(updated)
        student = self.db.find_student_by_pesel("50121373714")
        self.assertIsNotNone(student)
        self.assertEqual(student.first_name, "Jonathan")
        self.assertEqual(student.address, "New Address 42")


if __name__ == "__main__":
    unittest.main()

import unittest

from src.student import Student


class TestStudent(unittest.TestCase):
    def test_to_dict(self):
        student = Student("John", "Doe", "123 Main St", "12345", "92030512345", "M")
        expected = {
            "first_name": "John",
            "last_name": "Doe",
            "address": "123 Main St",
            "index_number": "12345",
            "pesel": "92030512345",
            "gender": "M",
        }
        self.assertEqual(student.to_dict(), expected)

    def test_from_dict(self):
        data = {
            "first_name": "Jane",
            "last_name": "Smith",
            "address": "456 Elm St",
            "index_number": "67890",
            "pesel": "85060712345",
            "gender": "F",
        }
        student = Student.from_dict(data)
        self.assertEqual(student.first_name, "Jane")
        self.assertEqual(student.last_name, "Smith")
        self.assertEqual(student.address, "456 Elm St")
        self.assertEqual(student.index_number, "67890")
        self.assertEqual(student.pesel, "85060712345")
        self.assertEqual(student.gender, "F")


if __name__ == "__main__":
    unittest.main()

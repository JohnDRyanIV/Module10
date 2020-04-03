import unittest
from class_definitions import student as s


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = s.Student("Dorna", "Jim", "Comp Sci")

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, "Dorna")
        self.assertEqual(self.student.first_name, "Jim")
        self.assertEqual(self.student.major, "Comp Sci")
        self.assertEqual(self.student.gpa, 0.00)

    def test_object_created_all_attributes(self):
        pass

    def test_student_str(self):
        pass

    def test_object_not_created_error_last_name(self):
        pass

    def test_object_not_created_error_first_name(self):
        pass

    def test_object_not_created_error_major(self):
        pass

    def test_object_not_created_error_gpa(self):
        pass


if __name__ == '__main__':
    unittest.main()

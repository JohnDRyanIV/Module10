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
        student = s.Student("Dorna", "Jim", "Comp Sci", 3.50)
        assert student.last_name == "Dorna"
        assert student.first_name == "Jim"
        assert student.major == "Comp Sci"
        assert student.gpa == 3.50

    def test_student_str(self):
        student = s.Student("Dorna", "Jim", "Comp Sci", 3.50)
        assert str(student) == "Dorna, Jim has major Comp Sci with gpa: 3.5"

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(TypeError):
            student = s.Student("Jim", "Comp Sci")
            student = s.Student("Jim", "Comp Sci", 3.50)
        with self.assertRaises(ValueError):
            student = s.Student("Jim", "Comp Sci", "3.50")
            student = s.Student("3.50", "Jim", "Comp Sci")
            student = s.Student(3.50, "Jim", "Comp Sci")


    def test_object_not_created_error_first_name(self):
        with self.assertRaises(TypeError):
            student = s.Student("Dorna", "Comp Sci")
            student = s.Student("Dorna", "Comp Sci", 3.50)
        with self.assertRaises(ValueError):
            student = s.Student("Dorna", "Comp Sci", "3.50")

    def test_object_not_created_error_major(self):
        with self.assertRaises(TypeError):
            student = s.Student("Dorna", "Jim")
            student = s.Student("Dorna", "Jim", 3.50)
        with self.assertRaises(ValueError):
            student = s.Student("Dorna", "Jim", "3.50")

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(TypeError):
            student = s.Student("Dorna", "Jim", "Comp Sci", "3.50")
        with self.assertRaises(ValueError):
            student = s.Student("Dorna", "Jim", "Comp Sci", 4.01)
            student = s.Student("Dorna", "Jim", "Comp Sci", 400)
            student = s.Student("Dorna", "Jim", "Comp Sci", -.01)



if __name__ == '__main__':
    unittest.main()

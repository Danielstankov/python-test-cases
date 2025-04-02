import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp1 = Employee("John", "Smith", 5000)
        self.emp2 = Employee("Harry", "Stone", 3000)
        self.emp1.apply_raise()
        self.emp2.apply_raise()

    def tearDown(self):
        pass

    def test_name(self):
        self.assertEqual(self.emp1.fullname(), "John Smith")
        self.assertEqual(self.emp2.fullname(), "Harry Stone")

    def test_email(self):
        self.assertEqual(self.emp1.email(), "John.Smith@email.com")
        self.assertEqual(self.emp2.email(), "Harry.Stone@email.com")

    def test_raise(self):
        self.assertEqual(self.emp1.pay, 5250)
        self.assertEqual(self.emp2.pay, 3150)

    def test_name_negative(self):
        self.assertNotEqual(self.emp1.fullname(), "JohnSmith")
        self.assertNotEqual(self.emp2.fullname(), "Harr Stone")

    def test_email_negative(self):
        self.assertNotEqual(self.emp1.email(), "John.Smith@gmail.com")
        self.assertNotEqual(self.emp2.email(), "Harry.Stark@email.com")

    def test_raise_negative(self):
        self.assertNotEqual(self.emp1.pay, 5000)
        self.assertNotEqual(self.emp2.pay, 3155)


if __name__ == '__main__':
    unittest.main()

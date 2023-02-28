import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        first_name = 'Karissa'
        last_name = 'Tysklind'
        salary = 50000
        self.custom_raise = 10000
        self.employee = Employee(first_name, last_name, salary)

    def test_give_default_raise(self):
        new_salary = self.employee.give_raise()
        self.assertEqual(new_salary, 55000)
    
    def test_give_custom_raise(self):
        new_salary = self.employee.give_raise(self.custom_raise)
        self.assertEqual(new_salary, 60000)

if __name__ == '__main__':
    unittest.main()
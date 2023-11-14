import unittest
from faker import Faker
from teacher.factory import TeacherFactory
from pprint import pprint

class TestTeacher(unittest.TestCase):
    def setUp(self):
        self.teachers = []
        
    
    def test_create_teacher(self):
        teacher = TeacherFactory()
        self.teachers.append(teacher)
        self.assertEqual(len(self.teachers), 1)
    
    def test_create_teachers(self):
        n = 5
        teachers = TeacherFactory.build_batch(n)
        self.teachers.extend(teachers)
        self.assertEqual(len(teachers), n)
        pprint(self.teachers, compact=True)
    
    def tearDown(self) -> None:
        self.teachers = []
        return super().tearDown()
        
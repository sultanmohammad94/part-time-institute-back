from typing import Optional
from datetime import datetime
from faker.providers import BaseProvider
from factory import Factory, Faker
from .models import Teacher



class EducationProvider(BaseProvider):
    def education_provider(self):
        return self.random_element(elements=['bachelor', 'master', 'phd', 'institution'])


Faker.add_provider(EducationProvider)

class TeacherFactory(Factory):
    class Meta:
        model = Teacher
    
    id: int = Faker('pyint')
    name: str = Faker('name')
    education: str = Faker('education_provider')
    created_at: datetime = datetime.now()
            
    
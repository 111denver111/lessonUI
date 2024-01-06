import random

from data.data import Person
from faker import Faker

faker_ru = Faker("ru_RU")
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=random.randint(1, 99),
        department=faker_ru.job(),
        salary=random.randint(10000, 100000)
    )

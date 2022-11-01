import faker.providers.address
from django.core.management.base import BaseCommand
from faker import Faker
from ttt.models import *
import random

DEP_NAMES = [
    "Департамент",
    "Управление",
    "Отдел",
    "Ячейка"
]

DEP_SUB = [
    "среды",
    "продажи",
    "кошек",
    "собак",
    "управления",
    "солнца",
    "луны",
    "леса",
    "джанго",
    "питона",
    "настольных игр",
    "серьезности",
    "лени",
    "музыки",
    "космоса",
    "антиквариата",
    "спорта",
    "единорогов",
    "сна",
    "живописи",
    "света"
    "логики",
    "трфаффик лайта"
]

class Provider(faker.providers.BaseProvider):
    def dep_subs(self):
        return self.random_element(DEP_SUB)

    def dep_names(self, level):
        return DEP_NAMES[level-2]

    def dep_full_name(self, level):
        return "%s %s" % (self.dep_names(level), self.dep_subs())


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        fake = Faker(["ru_RU"])
        fake.add_provider(Provider)

        dep_ids =  {
            1 : [1],
            2 : [],
            3 : [],
            4 : [],
            5 : []
        }

        for i in range(2,5):
            dep = Department.objects.create(
                name=fake.unique.dep_full_name(i),
                level=i,
                major_id=random.choice(dep_ids[i-1])
            )
            dep_ids[i].append(dep.id)

        for _ in range(60):
            lvl =random.choice(range(2,6))
            dep = Department.objects.create(
                name = fake.unique.dep_full_name(lvl),
                level = lvl,
                major_id= random.choice(dep_ids[lvl-1])
            )
            dep_ids[lvl].append(dep.id)

        dut_ids = []
        for _ in range(1000):
            dep_lvl = random.choice(range(1,6))
            dep_id = random.choice(dep_ids[dep_lvl])
            duty = Duty.objects.create(
                name = fake.job(),
                weight = random.choice(range(25)),
                department_id= dep_id
            )
            dut_ids.append(duty.id)

        for _ in range(50000):
            emp = Employer.objects.create(
                name = fake.name(),
                date_employment = fake.date(),
                salary = random.choice(range(6000, 500000)),
                duty_id= random.choice(dut_ids)
            )

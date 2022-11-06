from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200)
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    major = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    @property
    def description(self):
        dep_dict = {}
        dep_dict["id"] = self.id
        dep_emps = [e.get_employer_data for e in Employer.objects.filter(duty__department=self).order_by()]
        dep_dict["employers"] = dep_emps
        sub_deps = [(d.id, d.name) for d in Department.objects.filter(major_id=self.id)]
        dep_dict["sub_deps"] = sub_deps

        return dep_dict

    def __str__(self):
        return self.name

    class Mets:
        ordering = ["level"]

class Duty(models.Model):
    name = models.CharField(max_length=200)
    weight = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return "%s из %s" % (self.name, self.department.name)

    class Meta:
        verbose_name_plural = "Duties"

class Employer(models.Model):
    name = models.CharField(max_length=200)
    date_employment = models.DateField()
    salary = models.IntegerField()
    duty = models.ForeignKey(Duty, on_delete=models.CASCADE)

    @property
    def get_employer_data(self):
        emp_dict = {
            "name": self.name,
            "date": self.date_employment,
            "salary": self.salary,
            "duty": self.duty
        }
        return emp_dict

    def __str__(self):
        return self.name


from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200)
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    major = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Mets:
        ordering = ["level"]

class Duty(models.Model):
    name = models.CharField(max_length=200)
    weight = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return "%s of %s" % (self.name, self.department.name)

    class Meta:
        verbose_name_plural = "Duties"

class Employer(models.Model):
    name = models.CharField(max_length=200)
    date_employment = models.DateField()
    salary = models.IntegerField()
    duty = models.ForeignKey(Duty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


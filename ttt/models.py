from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200)
    level = models.IntegerField()
    major = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

class Duty(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Duties"

class Employer(models.Model):
    name = models.CharField(max_length=200)
    date_employment = models.DateTimeField()
    salary = models.IntegerField()
    duty = models.ForeignKey(Duty, on_delete=models.CASCADE)


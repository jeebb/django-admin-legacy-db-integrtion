from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'department'


class Employee(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'employee'
